cmd_/home/debian/Documents/practicos_SdC_2024/practico5/FuentesDrv2/Module.symvers :=  sed 's/ko$$/o/'  /home/debian/Documents/practicos_SdC_2024/practico5/FuentesDrv2/modules.order | scripts/mod/modpost -m      -o /home/debian/Documents/practicos_SdC_2024/practico5/FuentesDrv2/Module.symvers -e -i Module.symvers -T - 
