# eohackathon-better-ai
Contains material and instructions necessary to recreate the Machine Learning/AI hands-on exercises prepared for the BETTER project's session at the EO Joint Big Data Hackathon https://www.ec-better.eu/pages/h2020-eo-big-data-hackathon

Land cover changes and inter-annual vegetation performance analysis using ML algorithms

## Getting the experiment

This experiment is hosted in a software repository.

Use `git` to clone it:

```bash
cd /workspace
git clone https://github.com/ec-better/eohackathon-better-ai
cd better_ai
```

### Configuring the Python conda environment for experiment.ipynb

The file `env_dmuk_ml.yml` contains the Python conda environment for running the notebooks contained in this folder.

From the shell, run:

```bash
conda env create --file=env_dmuk_ml.yml
```

Once the environment configuration is done, you can activate it:

```bash
conda activate env_dmuk_ml
```

### Running the experiment

Open the `environment.ipynb` notebook and update the kernel to use `env_dmuk_ml`

Run the experiment by executing each of the cells with `shift` + `Enter`.

If asked for the credentials, provide your Ellip username and associated Ellip API key.

### Improving the experiment in a development branch

This experiment is under version control and uses the git flow method (see [https://datasift.github.io/gitflow/IntroducingGitFlow.html])

If not done previously, clone the experiment repository:

```bash
git clone https://github.com/ec-better/eohackathon-better-ai
cd better_ai
```

Then, checkout the `develop` branch with:

```bash
git checkout develop
```

At this stage, update the experiment.

When done:

```bash
git add -A
git commit -m '<commit message>'
git pull
```

Finally, do a release with:

```bash
ciop-release
```

## Getting the better ai


### Configuring the Python conda environment for BetterAI.ipynb

The file `env_better_ai.yml` contains the Python conda environment for running the notebooks contained in this folder.

From the shell, run:

```bash
conda env create --file=env_better_ai.yml
```

Once the environment configuration is done, you can activate it:

```bash
conda activate better_ai
```

### Running the betterAI

Open the `BetterAI.ipynb` notebook and update the kernel to use `better_ai`

Run the experiment by executing each of the cells with `shift` + `Enter`.

Good luck! 
