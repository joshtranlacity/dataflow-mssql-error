import apache_beam as beam
from apache_beam.pipeline import PipelineOptions

def run():
    pipeline_options = PipelineOptions()

    with beam.Pipeline(options=pipeline_options) as p:
        initialize = (
            p
            | "Initialize Pipeline" >> beam.Create([1,2,3,4,5])
        )

        _ = (
            initialize
            | "Print collection" >> beam.Map(print)
        )

if __name__ == '__main__':
    run()
    



