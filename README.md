# Stone masonry cross-section generator in 2D

The code is part of the S-RAY (Deep-Learning Sonic-RAY tomograpy for architectural heritage digital reconstruction and structural diagnosis) research project, 
supported by a fellowship from the Fundación General CSIC´s ComFuturo programme,
which has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 101034263.

## Quick start
First copy this repository to your pc running the following in your python terminal (Python 3.9 was used for its development)
```
git clone https://github.com/JavierOrtegaHeras/MasonryCrossSectionGenerator
```
Then install al required libraries using:
```
pip install -r requirements.txt
```

## Cross-section generator
The script will produce a 2D CAD drawing of a masonry cross section in *.dxf format.
The cross-section will be representative of an irregular stone masonry type with two leafs. 
The generated cross-sections are based on the real cross-sections of three stone masonry walls constructed at the laboratory (refer to https://doi.org/10.12688/openreseurope.15769.1).

![Figure 15](https://github.com/JavierOrtegaHeras/MasonryCrossSectionGenerator/assets/149710103/ee48a67f-5360-4c58-bd5c-d422392d430b)
<p align="center">Fig.1 - Elevations of the stone masonry walls constructed at the laboratory.</p>

</br>

![sections](https://github.com/JavierOrtegaHeras/MasonryCrossSectionGenerator/assets/149710103/8937002d-5203-49ba-85b3-371653d2d023)
<p align="center">Fig.2 - Example of cross-sections of the stone masonry walls constructed at the laboratory.</p>

</br>

The generated cross-sections will be similar to the following ones:
![sections_generated-03](https://github.com/JavierOrtegaHeras/MasonryCrossSectionGenerator/assets/149710103/d0fc041f-2afc-4689-bcb5-8c03314d6ea5)
<p align="center">Fig.2 - Example of automatically generated cross-sections of stone masonry walls using the script.</p>

The parameters to control in the script are: </br>
- Overall X and Y dimensions of the cross-section.
- Average stone/mortar percentage through factor K (from 0 to 1, being 1 full stone).
- Overall irregularity controlled by the sides of the polygon that forms the stone shape.
- The script will generate 2-3 stones per leaf.

</br>

The output will be n dxf files (one per cross-section generated) that will be stored in the output folder within the project.

## Licence
MasonryCrossSectioNGenerator is available under the Creative Commons Attribution 4.0 International license. See the LICENSE file for more info.
