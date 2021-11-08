#!/bin/bash
#JaLora
#Script Detiene bucle sin fin anterior

identi=$(ps | tr " " ":" | grep opcion1.sh | cut -d":" -f2 )
if [ -z $identi ] ;then
    echo "No existe"
else
    echo "Matando proceso"
    kill -9 $identi
    echo "Proceso eliminado"
fi
