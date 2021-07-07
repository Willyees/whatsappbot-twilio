# whatsappbot-twilio
Project to work with Twilio. Set up a bot to answer at incoming messages. In case specific strings are received, can reply differently
Can be useful to book footy matches organized on whatsapp, first come first served
Twilio to handle the messages redirection, Flask to set up a web api receiving messages from Twilio and applying the business logic.
To test, use ngrok so can easily interface the localhost project to the internet


Unfortunately, whatsapp API is very closed, so it is needed to utilise Twilio but to acheive the redirection of the messages in production, a business whatsapp account must be set up. 
That is not so immediate. Loads of forms to be filled and obviously a business set up
