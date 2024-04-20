FROM python

RUN mkdir /mygdtask

COPY bin/ /mygdtask

WORKDIR /mygdtask
# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./EmployeData.py"]