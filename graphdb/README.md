
GraphDB v0.01 Alpha (Python)

Author: 	Patryk Ząbkiewicz
e-mail:		pzabkiewicz@gmail.com

GraphDB is a sub-project for routing engine that provides
the graph database that can be queried for roads and junctions

 - Data are orginized in a series of BLOBs
 - BLOBS can be pointed to another BLOBs
 - BLOBa are orginized as a graph
 - Any BLOB can contain road specific data
 - BLOBS are stored as hashes
 - Hashes are stored in folders with two first letters
 - Database is copy-on-write
 - BLOBs are storing only interchanges between each other
 - Any BLOB containing the other BLOB within itself has refrence to the original

 - Tables and views are virtual sets of BLOBs
 - Relational model is only a virtual representation of data within database
 - Storage engine is a module that can be replaced
 - Query model is SQL

 - Partition data between nodes
 - Nodes don't know which one has data, they can only tell they don't have it
 - Map-Reduce algorithmic
 - 

