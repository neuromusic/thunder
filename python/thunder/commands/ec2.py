#!/usr/bin/env python

import os
import sys
import thunder

def main():
    spark = os.getenv('SPARK_HOME')
    if spark is None or spark == '':
        raise Exception('must assign the environmental variable SPARK_HOME with the location of Spark')

    if os.getenv('PYTHONPATH') is None:
        os.environ['PYTHONPATH'] = ""

    os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ":" + os.environ['SPARK_HOME'] + "/ec2/"
    os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ":" + os.environ['SPARK_HOME'] + "/ec2/third_party/boto-2.4.1.zip/boto-2.4.1"

    ec2script = os.path.join(os.path.dirname(os.path.realpath(thunder.__file__)), "utils/ec2.py")
    
    os.execv("python", ["python",ec2script]+sys.argv[1:])

if __name__ == "__main__":
    main()