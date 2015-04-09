#include <Python.h>

static const long long COIN = 100000000;



long long static GetBlockBaseValue(int nBits, int nHeight, bool fTestNet = false)
{
    long long nSubsidy = 10 * COIN;
	
    if (nHeight == 1){
		nSubsidy = 20000 * COIN;
	} else if (nHeight <= 100){
		nSubsidy = 1 * COIN;
	} else if (nHeight <= 5000){
		nSubsidy = 50 * COIN;
	} else if (nHeight <= 10000){
		nSubsidy = 40 * COIN;
	} else if (nHeight <= 15000){
		nSubsidy = 20 * COIN;
	}

    return nSubsidy;
}

static PyObject *ezoncoin_subsidy_getblockbasevalue(PyObject *self, PyObject *args)
{
    int input_bits;
    int input_height;
    if (!PyArg_ParseTuple(args, "ii", &input_bits, &input_height))
        return NULL;
    long long output = GetBlockBaseValue(input_bits, input_height);
    return Py_BuildValue("L", output);
}

static PyObject *ezoncoin_subsidy_getblockbasevalue_testnet(PyObject *self, PyObject *args)
{
    int input_bits;
    int input_height;
    if (!PyArg_ParseTuple(args, "ii", &input_bits, &input_height))
        return NULL;
    long long output = GetBlockBaseValue(input_bits, input_height, true);
    return Py_BuildValue("L", output);
}

static PyMethodDef ezoncoin_subsidy_methods[] = {
    { "GetBlockBaseValue", ezoncoin_subsidy_getblockbasevalue, METH_VARARGS, "Returns the block value" },
    { "GetBlockBaseValue_testnet", ezoncoin_subsidy_getblockbasevalue_testnet, METH_VARARGS, "Returns the block value for testnet" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initezoncoin_subsidy(void) {
    (void) Py_InitModule("ezoncoin_subsidy", ezoncoin_subsidy_methods);
}
