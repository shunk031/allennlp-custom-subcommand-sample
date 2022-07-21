# AllenNLP sample code for Subcommand

This is a AllenNLP sample code for the Subcommand mechanism.

The registrable subcommand mechanism is a feature introduced in the PR ([allenai/allennlp#3671](https://github.com/allenai/allennlp/pull/3671)).
The original allennlp has subcommands such as `train`, `evaluate`, and `predict`. This sample code shares how to define your own subcommands.

## Execution example

```shell
$ allennlp --help
2022-07-13 22:12:44,209 - INFO - allennlp.common.plugins - Plugin my_project available << You can find the my_project lib is automatically loaded!
usage: allennlp [-h] [--version]  ...

Run AllenNLP

optional arguments:
  -h, --help        show this help message and exit
  --version         show program's version number and exit

Commands:

    build-vocab     Build a vocabulary from an experiment config file.
    cached-path     Cache remote files to the AllenNLP cache.
    checklist       Run a trained model through a checklist suite.
    count-instances
                    Count the number of training instances in an experiment config file.
    diff            Display a diff between two model checkpoints.
    evaluate        Evaluate the specified model + dataset(s).
    find-lr         Find a learning rate range.
    predict         Use a trained model to make predictions.
    print-results   Print results from allennlp serialization directories to the console.
    push-to-hf      Push a model to the Hugging Face Hub. Pushing your models to the Hugging Face Hub ([hf.co](https://hf.co/)) allows you to share your models with others. On top of that, you can try the models directly in the browser with the available widgets. Before running this command, login to Hugging Face with `huggingface-cli login`. You can specify
                    either a `serialization_dir` or an `archive_path`, but using the first option is recommended since the `serialization_dir` contains more useful information such as metrics and TensorBoard traces.
    test-install    Test AllenNLP installation.
    train           Train a model.
    hello-subcommand                                    << Here is the command that have been added!
                    This is the first custom subcommand << Here is the command that have been added!
```

```shell
$ allennlp hello-subcommand --message world!
2022-07-13 22:09:51,665 - INFO - allennlp.common.plugins - Plugin my_project available
Hello world!
```

## Tips for adding custom subcommand

I recommend that you also refer to [allenai/allennlp-template-config-files](https://github.com/allenai/allennlp-template-config-files ), a template for starting a new allennlp project using config files and `allennlp train`.

### Create `.allennlp_plugins`

- Create `.allennlp_plugins` file in the root directory of the project (ref. [9d487b7](https://github.com/shunk031/allennlp-custom-subcommand-sample/commit/9d487b7259b5a5f77f9d1ba5f5a14338293120cf)).
- Add custom library name e.g., `my_project` to the `.allennlp_plugins` in the project.

| Create `.allennlp_plugins` | Add custom library name, e.g., `my_project` |
|------|------|
|![](https://user-images.githubusercontent.com/11523725/178748427-f7a2359c-38c6-4bd1-abd3-7dc7ff448232.png)| ![](https://user-images.githubusercontent.com/11523725/178748889-803c115b-1416-465c-b3f4-a0c2ba78bafc.png)  |

### Create files under `my_project/commands`

- Create files for the `hello-subcommand` command under the `my_project/commands`
  - I recommend to create two files: [`sub_command.py`](https://github.com/shunk031/allennlp-custom-subcommand-sample/blob/master/my_project/commands/hello_subcommand/sub_command.py) for the registrable subcommand and [`function.py`](https://github.com/shunk031/allennlp-custom-subcommand-sample/blob/master/my_project/commands/hello_subcommand/function.py) for main function for the subcommand.
  - You must remember to create `__init__.py` in each sub directories.

![](https://user-images.githubusercontent.com/11523725/178749218-3602dbab-052a-478d-bcce-422edccf677e.png)

### Update files to load the subcommand

- Update `my_project/__init__.py` to load `my_project/commands`.
- Update `my_project/commands/__init__.py` to load `my_project.commands.sub_command.HelloSubcommand`.

| [`my_project/__init__.py`](https://github.com/shunk031/allennlp-custom-subcommand-sample/blob/master/my_project/__init__.py) | [`my_project/commands/__init__.py`](https://github.com/shunk031/allennlp-custom-subcommand-sample/blob/master/my_project/commands/__init__.py) |
|------|------|
| ![](https://user-images.githubusercontent.com/11523725/178749472-ff638215-772c-4b47-b609-c5541dc6db14.png) | ![](https://user-images.githubusercontent.com/11523725/178749631-ad633671-3596-467c-8c1a-512a43498244.png) |

That's all. Now you can realize all your ideas as subcommands 🎉

## Mechanism of automatically registering/loading the subcommand

The following is a rough introduction to the mechanism:

1. allennlp reads `.allennlp_plugins` in the repository root.
2. Based on the library name (e.g., `my_project` in this repository) in `.allennlp_plugins`, load the `__init__.py` (e.g., `my_project/__init__.py`) of the root of that library.
3. The `__init__.py` has imported the custom subcommand so that allennlp can register that subcommand.

# Acknowledgments

- allenai/allennlp: An open-source NLP research library, built on PyTorch. https://github.com/allenai/allennlp 
- allenai/allennlp-template-config-files: A template for starting a new allennlp project using config files and `allennlp train` https://github.com/allenai/allennlp-template-config-files 
