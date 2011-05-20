
PROJECT = sansmodel

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	CylinderModel.py \
	IQComputation.py \
	SphereModel.py \
	__init__.py \


export:: export-python-modules
