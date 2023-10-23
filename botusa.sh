if [[ "1" = "$1" ]]; then
  hora=60
elif [[ "2" = "$1" ]]; then
  hora=120
elif [[ "3" = "$1" ]]; then
  hora=180
elif [[ "4" = "$1" ]]; then
  hora=240
elif [[ "5" = "$1" ]]; then
  hora=300
elif [[ "6" = "$1" ]]; then
  hora=360
else
  echo "Error: solo se puede establecer de 1 a 6 horas, aplicando cambios automáticos..."
  echo "Inicie de nuevo el código"
  exit
fi

git config --global user.email "u22216510@utp.edu.pe"
git config --global user.name "FabriSC" 
git config --global pull.rebase false
git config --global credential.helper store
echo "https://FabriSC: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@github.com" > .git-credentials

sed -i "s/hori/$hora/g" .github/workflows/MirrorSC.yml
sed -i "s/horo/$1/g" .github/workflows/MirrorSC.yml

git add -f .
git commit -m "Activando: $1 horas,numero de activacion: $RANDOM"
git push
rm -rf .github/workflows/MirrorSC.yml
cp .github/MirrorSCb.yml .github/workflows/MirrorSC.yml
exit