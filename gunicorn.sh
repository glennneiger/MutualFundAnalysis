nohup gunicorn MutualFundAnalysis.wsgi:application -b 0.0.0.0:12000 --reload &