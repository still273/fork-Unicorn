
#***************************************************************************************
# 2:1:7 split gold
entity_alignment_data = { 
    "dbp_yg": ["train", "fork-unicorn/data/dbp_yg/", "hit"],
    "dbp_wd": ["test", "fork-unicorn/data/dbp_wd/", "hit"]
}

# 2:1:7
string_matching_data = { 
    "smurf1":["train", "fork-unicorn/data/smurf-addr/", "f1"],
    "smurf2":["train", "fork-unicorn/data/smurf-names/", "f1"],
    "smurf3":["train", "fork-unicorn/data/smurf-res/", "f1"],
    "smurf4":["test", "fork-unicorn/data/smurf-prod/", "f1"],
    "smurf5":["train", "fork-unicorn/data/smurf-cit/", "f1"]
}

# 3:1:1 directly use
new_deepmatcher_data = { 
    #"m1":["train","fork-unicorn/data/em-wa/", "f1"],
    "m2":["test","fork-unicorn/data/em-ds/", "f1"],
    "m3":["train","fork-unicorn/data/em-fz/", "f1"],
    "m4":["train","fork-unicorn/data/em-ia/", "f1"],
    "m5":["train","fork-unicorn/data/em-beer/", "f1"]
    
}

# 2:1:7 
new_schema_matching_data = { 
    "fab": ["train", "fork-unicorn/data/fabricated_dataset/", "recall"],
    "deepmdatasets": ["test","fork-unicorn/data/DeepMDatasets/", "recall"],
}

# 2:1:7 
ontology_matching_data = {
    "cw":["train", "fork-unicorn/data/Illinois-onm/", "acc"]
}

# 2:1:7 
column_type_data = {
    "efth":["train","fork-unicorn/data/efthymiou/", "acc"],
    "t2d":["train", "fork-unicorn/data/t2d_col_type_anno/", "acc"],
    "limaya":["test", "fork-unicorn/data/Limaye_col_type_anno/", "acc"]
}

# 2:1:7 
entity_linking_data = {
    "t2d":["train","fork-unicorn/data/t2d/", "f1"],
    "limaya":["test", "fork-unicorn/data/Limaye/", "f1"]
}
