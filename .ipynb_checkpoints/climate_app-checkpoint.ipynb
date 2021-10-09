{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d1423533",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "from dateutil.relativedelta import relativedelta\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5227c0f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f853bd48",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine('sqlite:///hawaii.sqlite', connect_args={'check_same_thread': False})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "54992509",
   "metadata": {},
   "outputs": [],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2904e189",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurements",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    185\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 186\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'measurements'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-12-7fbdbc5a958e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Save references to the tables\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mMeasurement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmeasurements\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mStation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstations\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    186\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 188\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    189\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    190\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: measurements"
     ]
    }
   ],
   "source": [
    "# Save references to the tables\n",
    "Measurement = Base.classes.measurements\n",
    "Station = Base.classes.stations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "34900c8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b0f737f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4be08c3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "last_twelve_months = '2016-08-23'\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"<p>Welcome to the Hawaii weather API!</p>\"\n",
    "        f\"<p>Usage:</p>\"\n",
    "        f\"/api/v1.0/precipitation<br/>Returns a JSON list of percipitation data for the dates between 8/23/16 and 8/23/17<br/><br/>\"\n",
    "        f\"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17<br/><br/>\"\n",
    "        f\"/api/v1.0/date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17<br/><br/>.\"\n",
    "        f\"/api/v1.0/start_date/end_date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date<br/><br/>.\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e6362e0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    # Date 12 months ago\n",
    "    p_results = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= last_twelve_months).group_by(Measurement.date).all()\n",
    "    return jsonify(p_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "eee9203b",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    s_results = session.query(Station.station, Station.name).all()\n",
    "    return jsonify(s_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "76404e27",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    t_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= last_twelve_months).all()\n",
    "    return jsonify(t_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "34a3ea44",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/<date>\")\n",
    "def startDateOnly(date):\n",
    "    day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date).all()\n",
    "    return jsonify(day_temp_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f33aebc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def startDateEndDate(start,end):\n",
    "    multi_day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()\n",
    "    return jsonify(multi_day_temp_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3d4b1837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      " * Restarting with fsevents reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/IPython/core/interactiveshell.py:3445: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa68617d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
