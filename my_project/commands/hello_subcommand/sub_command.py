import argparse

from allennlp.commands.subcommand import Subcommand

from .function import hello_function


@Subcommand.register("hello-subcommand")
class HelloSubcommand(Subcommand):
    def add_subparser(
        self, parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:

        description = "custom subcommand for just say hello with your message"

        # create subparser from the parser
        subparser = parser.add_parser(
            self.name,
            description=description,
            help="This is the first custom subcommand",
        )
        # add arguments
        subparser.add_argument("--message", type=str, default="world")

        # set the function to be called when this subcommand is executed.
        subparser.set_defaults(func=lambda args: hello_function(msg=args.message))

        return subparser
