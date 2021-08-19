RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function stop_container() {
    if [ "$(docker ps -q -f name="$1")" ]; then
        echo "Stopping container $1"
        docker container stop "$1"
    fi
}

function validate_configuration_file() {

  CONFIG_FILE=$1
  REQUIRED_VARIABLES=$2

  echo "-> Required environment variables: "

  for i in "${!REQUIRED_VARIABLES[@]}"; do
    echo "        ${REQUIRED_VARIABLES[$i]}"
  done

  echo
  echo "Validating ${CONFIG_FILE}..."
  echo

  config_is_valid=1

  config_keys=()
  config_values=()

  while IFS="=" read -r detected_key detected_value; do

      if [ -z "$detected_key" ] || [ -z "$detected_value" ] ; then
          continue
      fi

      config_keys+=("$detected_key")
      config_values+=("$detected_value")

  done < "$CONFIG_FILE"

  for i in "${!REQUIRED_VARIABLES[@]}"; do

    required_variable=${REQUIRED_VARIABLES[$i]}
    variable_exists=0

    for j in "${!config_keys[@]}"; do
        config_key=${config_keys[$j]}
        config_value=${config_values[$j]}

        if [ "${config_key}" == "${required_variable}" ] && [ -n "$config_value" ]; then
             variable_exists=1
             break
        fi
    done

    if [ $variable_exists == 1 ]; then
      echo -e "${GREEN}${required_variable} exists${NC}"
    else
      echo -e "${RED}${required_variable} missing or empty${NC}"
      config_is_valid=0
      break
    fi

  done

  if [ $config_is_valid == 0 ]; then
    echo
    echo -e "${RED}Config is not valid. Exiting${NC}"
    exit 1
  fi
}

function check_file_exists() {
  FILE=$1

  if [ ! -f "$FILE" ]; then
    echo "Error: $FILE not found. Exiting."
    exit 0
  fi
}

function unlock_api_persistence() {
  if [[ -d "persistence" ]]; then
    sudo chown -R 1000:1000 persistence
  fi
}