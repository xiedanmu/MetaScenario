# MetaScenario
MetaScenario: A Framework for Driving Scenario Data Description, Storage and Indexing
---

## Introduction
![Image](https://github.com/THU-changc17/MetaScenario/blob/main/Visualization/DataBase.jpg)

MetaScenario is a unified framework for driving scenario data. We describe driving scenarios and design the centralized and unified data framework for storage, processing, and indexing of scenario data based on relational database.

The concept of atom scenario is proposed and characterized using semantic graphs. We also annotate and classify behaviors of traffic participants in atom scenarios by extracting the spatial-temporal evolution of semantic information. The annotation facilitates the indexing and extraction of data, which allows the evaluation of the
scenario datasets using data distribution and annotation statistics. 

MetaScenario can provide researchers with a convenient tool for scenario data extraction and important analytical references.

## Compatible Scenario Datasets
Based on the MetaScenario framework, we adapt and 
store the typical scenario datasets to implement the data adaptation without losing the information 
and accuracy of the original dataset.

Here we select four typical traffic scenario datasets, NGSIM, HighD, Argoverse, and Interaction to demonstrate the data adaptation work.

Considering the licensing of the datasets, we do not upload the original datasets here. Researchers can obtain the datasets through registration or application.
The URLs of the relevant datasets are as follows:

[NGSIM](https://ops.fhwa.dot.gov/trafficanalysistools/ngsim.htm) &nbsp; [HighD](https://www.highd-dataset.com/) &nbsp; [InD](https://www.ind-dataset.com/)
&nbsp; [Interaction](http://interaction-dataset.com/)  &nbsp; [Argoverse](https://www.argoverse.org/data.html)

## Usage
Let's take the Interaction Merging DataSet as example.

### Requirements
MySQL >= 5.7

Python 3.6

### Data Storage

Check the MetaScenario project folder has been included in sys.path and get started.
`cd InsertDataBase`

Modify the DB name and create new DB.
`python CreateDB.py --DB Interaction_MergingZS_Scenario_DB`

Please modify the dataset folder location. 

Store the road environment data into database.
`python Interaction_MergingZS_InsertMap.py --DB Interaction_MergingZS_Scenario_DB --File ../DataSet/INTERACTION-Dataset-DR-v1_1/maps/DR_CHN_Merging_ZS.osm`

Store the traffic participant data into database.
`python Interaction_MergingZS_InsertTrafficParticipant.py --DB Interaction_MergingZS_Scenario_DB --Table 0 --File ../DataSet/INTERACTION-Dataset/vehicle_tracks_000.csv
`

Add the foreign key in the database.
`python Alter_ForeignKey.py --DB Interaction_MergingZS_Scenario_DB --Table 0`

Note: The map foreignkey should be added only once and 
the participant foreignkey can be added when users store new participant data file.

### Data Visulization
We also implement a common visualization program interface based on the unified database framework to facilitate
researchers to visually observe the driving scenarios embodied in each dataset(refer to [map_visualization](https://github.com/THU-changc17/MetaScenario/blob/main/map_visualization.py) 
and [vehicle_visualization](https://github.com/THU-changc17/MetaScenario/blob/main/vehicle_visualization_v2.py)).

`python vehicle_visualization_v2.py --DB Interaction_MergingZS_Scenario_DB --Table 0`

![Image](https://github.com/THU-changc17/MetaScenario/blob/main/Visualization/Merging.png)

### Scene Graph Converter
In vehicle trajectory prediction and planning research field, many researchers currently favor the format of scene snapshot
images for their input data. Similar to the format provided by the official [Lyft dataset](https://level-5.global/data/), our data framework
can support a convenient conversion to this format.

`python scene_image_snapshot.py --DB Interaction_MergingZS_Scenario_DB --Table 0 --Ego 20 --Timestamp 1000 --Interval 1000`

<div align=center><img src="https://github.com/THU-changc17/MetaScenario/blob/main/Visualization/snapimage.png"/></div>

### Atom Scenario Characterization
To characterize the atom scenarios, we use the structure of
semantic graphs. We need a range of space and time parameters, a
vehicle as ego vehicle, and establish a semantic graph to give a
description of the relationship and state between ego vehicle
and surrounding elements (referring to the components of the
traffic scenario such as vehicles, road network nodes, and lanes).

Users need to select or define the parameters in [relation_extractor](https://github.com/THU-changc17/MetaScenario/blob/main/relation_extractor.py)

Generate the scene graph, which is a frame of atom scenario `python scene_graph_visualization.py --DB Interaction_MergingZS_Scenario_DB --Table 0 --Ego 17 --Timestamp 1000`

![Img](https://github.com/THU-changc17/MetaScenario/blob/main/AtomScenarioGraph/17_1000.jpg)

### Data Annotation

We also annotate NGSIM, HighD, Argoverse, and Interaction
datasets stored in the data framework through the temporal and
spatial evolution of the semantic graph, including the begin and
end timestamp of captured scenario fragments, the driving
behaviors generated by the vehicle and interaction with
adjacent traffic participants.

`cd Annotator`

`python Interaction_Merge_Anotator.py --DB Interaction_MergingZS_Scenario_DB --Table 0`

The annotation results will be recorded in Scenario_Behavior_Index Table.

## Citation
If you find our work is useful in your research, please consider citing:
```
@article{chang2022metascenario,
  title={Metascenario: A framework for driving scenario data description, storage and indexing},
  author={Chang, Cheng and Cao, Dongpu and Chen, Long and Su, Kui and Su, Kuifeng and Su, Yuelong and Wang, Fei-Yue and Wang, Jue and Wang, Ping and Wei, Junqing and Wu, Gansha and Wu, Xiangbin and Xu, Huile and Zheng, Nanning and Li, Li},
  journal={IEEE Transactions on Intelligent Vehicles},
  volume={8},
  number={2},
  pages={1156--1175},
  year={2022},
  publisher={IEEE}
}
```
