readme.md
Readme for asagi / foolfuuka image zip tool



===== USAGE =====
Example usage:
python step1_dump_img_table.py sqlalchemy_connect_string table_name path_to_csv_file lower_bound
python step1_dump_img_table.py "mysql://root:toor@localhost/asagi_exporter" "gif_images" "data/mysql_gif.csv" "1536638719722.webm"

python step2_zip.py path_to_csv_file images_dir path_to_output_zip_file boardname
python step2_zip.py "data/mysql_gif.csv" "images/" "data/mysql_gif_images.zip" "g"