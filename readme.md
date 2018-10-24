readme.md
Readme for asagi / foolfuuka image zip tool



===== USAGE =====
Example usage:

Step 1:
Template:
python step1_dump_img_table.py --connection_string="" --table_name="" --csv_filepath="" --lower_bound=""
Example:
python step1_dump_img_table.py --connection_string="mysql://root:toor@localhost/asagi" --table_name="gif_images" --csv_filepath="data/mysql_gif_images.csv" --lower_bound="1536638719722.webm"


Step 2:
Template:
python step2_zip.py --csv_filepath="" --images_dir="" --path_to_output_zip_file="" --boardname=""
Example:
python step2_zip.py --csv_filepath="data/mysql_gif_images.csv" --images_dir="/var/www/foolfuuka/public/foolfuuka/boards/" --zip_path="data/mysql_gif_images.zip" --boardname="g"



===== INSTALLATION =====

Linux (only tested on ubuntu 16 lts):

sudo apt-get install python-pip python-dev libmysqlclient-dev
pip install requests
pip install sqlalchemy
pip install mysqlclient




