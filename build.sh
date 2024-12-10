cd theme/static_src
npm install
npm run build
cd ../..
python manage.py collectstatic --noinput