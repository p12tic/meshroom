__version__ = "1.0"

from meshroom.core import desc

class SplitDoubleFisheye(desc.CommandLineNode):
    commandLine = 'aliceVision_utils_splitDoubleFisheye {allParams}'
    
    category = 'Utils'
    documentation = '''This node is used to split double fisheye images'''

    inputs = [
        desc.File(
            name='input',
            label='SfmData',
            description='SfmData File',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='output1',
            label='First Output SfMData File',
            description='Path to the output sfmdata file for the first part',
            value=desc.Node.internalFolder + 'cameras_part1.sfm',
            uid=[],
        ),
        desc.File(
            name='output2',
            label='Second Output SfMData File',
            description='Path to the output sfmdata file for the second part',
            value=desc.Node.internalFolder + 'cameras_part2.sfm',
            uid=[],
        )
    ]
