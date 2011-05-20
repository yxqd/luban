
PROJECT = plotfx

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	CurveComputation.py \
	Exponential.py \
	Functor.py \
	Sin.py \
	__init__.py \


export:: export-python-modules
