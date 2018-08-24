# KML Parser

A kml to json parser meant for converting kml file with city neighborhood boundaries into JSON objects used in my city neighborhood viewer. Instead of using the out of box python XML parser, I used regular expressions to develop my experience with them.

See "San Francisco Neighborhood map.kml" then sfCoords.js for before and after effects of this parser. Alternitvely see below:

Before:

```
<Placemark>
        <name>Forest Knolls</name>
        <styleUrl>#poly-0000FF-3000-115-nodesc</styleUrl>
        <Polygon>
          <outerBoundaryIs>
            <LinearRing>
              <tessellate>1</tessellate>
              <coordinates>
                -122.452497,37.758332,0
                -122.452583,37.759384,0
                -122.453055,37.761691,0
                -122.454343,37.760978,0
                -122.455201,37.760334,0
                -122.45636,37.761623,0
                -122.457433,37.76186,0
                -122.45842,37.761792,0
                -122.460179,37.759044,0
                -122.463913,37.758603,0
                -122.463613,37.75521,0
                -122.463999,37.75409,0
                -122.463527,37.753242,0
                -122.46254,37.75236,0
                -122.461767,37.751512,0
                -122.461166,37.751783,0
                -122.459064,37.752021,0
                -122.457347,37.751478,0
                -122.456532,37.751512,0
                -122.456102,37.751851,0
                -122.456059,37.753039,0
                -122.455158,37.754362,0
                -122.455029,37.75521,0
                -122.454085,37.756771,0
                -122.453828,37.757585,0
                -122.453012,37.758026,0
                -122.452497,37.758332,0
              </coordinates>
            </LinearRing>
          </outerBoundaryIs>
        </Polygon>
      </Placemark>
 ```

 After:

 ```
 "Forest Knolls": {
	coords:[{
		lat: 37.758332,
		lng: -122.452497
	}, {
		lat: 37.759384,
		lng: -122.452583
	}, {
		lat: 37.761691,
		lng: -122.453055
	}, {
		lat: 37.760978,
		lng: -122.454343
	}, {
		lat: 37.760334,
		lng: -122.455201
	}, {
		lat: 37.761623,
		lng: -122.45636
	}, {
		lat: 37.76186,
		lng: -122.457433
	}, {
		lat: 37.761792,
		lng: -122.45842
	}, {
		lat: 37.759044,
		lng: -122.460179
	}, {
		lat: 37.758603,
		lng: -122.463913
	}, {
		lat: 37.75521,
		lng: -122.463613
	}, {
		lat: 37.75409,
		lng: -122.463999
	}, {
		lat: 37.753242,
		lng: -122.463527
	}, {
		lat: 37.75236,
		lng: -122.46254
	}, {
		lat: 37.751512,
		lng: -122.461767
	}, {
		lat: 37.751783,
		lng: -122.461166
	}, {
		lat: 37.752021,
		lng: -122.459064
	}, {
		lat: 37.751478,
		lng: -122.457347
	}, {
		lat: 37.751512,
		lng: -122.456532
	}, {
		lat: 37.751851,
		lng: -122.456102
	}, {
		lat: 37.753039,
		lng: -122.456059
	}, {
		lat: 37.754362,
		lng: -122.455158
	}, {
		lat: 37.75521,
		lng: -122.455029
	}, {
		lat: 37.756771,
		lng: -122.454085
	}, {
		lat: 37.757585,
		lng: -122.453828
	}, {
		lat: 37.758026,
		lng: -122.453012
	}, {
		lat: 37.758332,
		lng: -122.452497
	}]}
 ```



## Built With

* [python 2.7](https://www.python.org/download/releases/2.7/) - The web framework used

## Contributing

Feel free to make any change or improvement you see fit. Provide ample detail of your changes at the bottom of the README for review. 

## Versioning

[SemVer](http://semver.org/) is used for versioning. 

V 1.0

## Authors

* **Leslie Jones-Dove** [Lazlojd](https://github.com/lazlojd)


