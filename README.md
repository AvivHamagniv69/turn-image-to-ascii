# turn-image-to-ascii
takes a provided image and makes a .txt file with the image drawn in ascii characters

# examples: 
## original image:
![mario](https://user-images.githubusercontent.com/51734410/196738211-15f0d688-c5a6-40a2-bbba-a215015df8c6.jpg) 

## basic ascii table:
![Screenshot_20221019_183522](https://user-images.githubusercontent.com/51734410/196738083-60bcaa2f-69e7-4a53-8645-de6acd53ba64.png)

## flat ascii table:
![Screenshot_20221110_235225](https://user-images.githubusercontent.com/51734410/201214006-16602d63-dbea-4f01-9a58-78981cb51d01.png)

## complex ascii table (dosent look good until i add a better convertion algorithm from pixel to ascii but i wanted to implement it anyways):
![Screenshot_20221110_235754](https://user-images.githubusercontent.com/51734410/201214517-a745733c-e753-4c21-8d90-1d5d18f3101c.png)

## dependencies:
you need pillow which comes with python 3 as far as im aware but it gave me problems so if it does it to you try running the install command again (this is for linux):

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## how to use:
you type the following command into the terminal and you get a file as an output:
```
python3 ascii.py size_of_ascii_image /optional_path_to_file/name_of_file /optional_path_to_file/name_of_output_file
```

### side note:
while this *technically* works on windows it dosent draw the image correctly and for now i cant fix it, but hopefuly you can fix it
