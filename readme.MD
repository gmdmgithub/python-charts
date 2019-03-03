# simple playground with folium and bokeh libraries

## If no installed pipenv - install - other solution docker (another scafold)
```
pip install pipenv
```
## Activate pipenv
```
pipenv shell
```
## for environment variables
```
pipenv install python-dotenv
```
# maps - using folium, its powerfull library with using opensource maps

## install
```
pipenv install fulium
```
## Use as map
```
map = folium.Map(location=[X,Y], zoom_start=<NUM>)
...
map.save('index.html')
```
# Run project with pipenv ie:
```
pipenv run maps.py
```
## Use charts - powerful bokeh library
```
pipenv install bokeh pandas
```
### Find bokeh lib https://bokeh.pydata.org/

## Version
1.0.0
## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
