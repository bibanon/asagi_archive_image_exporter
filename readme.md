readme.md
Readme for asagi / foolfuuka image zip tool



===== USAGE =====
Example usage:
python step1_dump_img_table.py sqlalchemy_connect_string table_name path_to_csv_file lower_bound
python step1_dump_img_table.py "mysql://root:toor@localhost/asagi_exporter" "gif_images" "data/mysql_gif_images.csv" "1536638719722.webm"

Step 1:
Template:
python step1_dump_img_table.py --sqlalchemy_connect_string="" --table_name="" --path_to_csv_file="" --lower_bound=""
Example:
python step1_dump_img_table.py --sqlalchemy_connect_string="mysql://root:toor@localhost/asagi" --table_name="gif_images" --path_to_csv_file="data/mysql_gif_images.csv" --lower_bound="1536638719722.webm"






python step2_zip.py path_to_csv_file images_dir path_to_output_zip_file boardname

python step2_zip.py "data/mysql_gif_images.csv" "/var/www/foolfuuka/public/foolfuuka/boards/" "data/mysql_gif_images.zip" "g"

Step 2:
Template:
python step2_zip.py --path_to_csv_file="" --images_dir="" --path_to_output_zip_file="" --boardname=""
Example:
python step2_zip.py --path_to_csv_file="data/mysql_gif_images.csv" --images_dir="/var/www/foolfuuka/public/foolfuuka/boards/" --path_to_output_zip_file="data/mysql_gif_images.zip" --boardname="g"



===== INSTALLATION =====

Linux (only tested on ubuntu 16 lts):

sudo apt-get install python-pip python-dev libmysqlclient-dev
pip install requests
pip install sqlalchemy
pip install mysqlclient




