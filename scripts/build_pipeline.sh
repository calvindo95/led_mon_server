if [ $# -lt 0 ]; then # checks if number of arguments is less than 1
    echo "Usage: 'sh pipeine.sh"
    return 1
fi

BASE_IMG="led_mon_server-base-img"
FINAL_IMG="led_mon_server-img"
CONTAINER_NAME="led_mon_server"

BASE_DOCKERFILE="scripts/Dockerfile_base_img_x86"
FINAL_DOCKERFILE="scripts/Dockerfile_img_x86"

if $(docker image ls | grep -q ${BASE_IMG})
then
    echo "${BASE_IMG} img exists, building ${FINAL_IMG}"
    sh scripts/build_img.sh ${FINAL_DOCKERFILE} ${FINAL_IMG}

    if $(docker ps | grep -q ${CONTAINER_NAME})
    then
        echo "${CONTAINER_NAME} still active, stopping."
        sh scripts/stop.sh ${CONTAINER_NAME}
    else
        echo "${FINAL_IMG} already stopped."
    fi

    yes | docker container prune

    sh scripts/spinup.sh ${FINAL_IMG} ${CONTAINER_NAME}
else
    echo "${BASE_IMG} img does not exist, building base img"
    sh scripts/build_img.sh ${BASE_DOCKERFILE} ${BASE_IMG}
fi