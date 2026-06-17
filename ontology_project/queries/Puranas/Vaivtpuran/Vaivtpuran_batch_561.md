# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 39.8239)
- **Original**: बहुमूल्य रज्नोंके बने हुए सैकड़ों मन्दिर दीख पड़े, सिद्धविद्यामें अत्यन्त निपुण पुण्यवान्‌ सिद्धोंद्वारा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8240)
- **Original**: जो अमूल्य रत्रों्वारा निर्मित चमचमाते हुए कलशोंसे सेवित था। जो तीन लाख योजन ऊँचे और सौ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8241)
- **Original**: सुशोभित थे। अमूल्य रत्नोंके बने हुए किवाड़, योजनके विस्तारवाले थे। जिनमें सैकड़ों मोटी-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8242)
- **Original**: जिनमें होरे जड़े हुए थे और मोतियाँ एवं निर्मल मोटी डालियाँ थीं, जो असंख्य शाखासमूहों और शीशे लगे हुए थे, उन मन्दिरोंकी शोभा बढ़ा रहे असंख्य फलोंसे संयुक्त थे। परम मनोहर शब्द
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8243)
- **Original**: थे। उनमें गोरोचना नामक मणियोंके हजारों खंभे करनेवाले विभिन्न प्रकारके पश्षिसमूहोंसे व्याप्त थे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8244)
- **Original**: लगे थे और वे मणियोंकी सीढ़ियोंसे सम्पन्न थे। शीतल-सुगन्ध वायु जिन्हें कम्पायमान कर रही
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8245)
- **Original**: परशुरामने उनके भीतरी द्वारकों देखा, जो नाना थी, ऐसे अविनाशी वरवृक्षोंसे, सहस्रों पुष्पोद्यानोंसे,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8246)
- **Original**: प्रकारकी चित्रकारीसे चित्रित तथा हीरे-मोतियोंकी सैकड़ों सरोबरोंसे तथा मणियों एवं रत्रोंसे बने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8247)
- **Original**: गुँथी हुई मालाओंसे सुशोभित था। उसको बार्यी हुए सिद्धेन्दोंके लाखों भवनोंसे वह नगर सुशोभित
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8248)
- **Original**: ओर कार्तिकेय और दाहिनी ओर गणेश तथा था। उसे देखकर परशुरामका मन अत्यन्त
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8249)
- **Original**: शिव-तुल्य पराक्रमी विशालकाय वीरभद्र दीख प्रसन्नतासे खिल उठा। फिर सामने ही उन्हें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8250)
- **Original**: पड़े। नारद! वहाँ प्रधान-प्रधान पार्षद और क्षेत्रपाल शंकरजीका शोभाशाली रमणीय आश्रम दीख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8251)
- **Original**: भी रत्राभरणोंसे विभूषित हो रत्ननिर्मित सिंहासनोंपर पड़ा। विश्वकर्माने बहुमूल्य सुनहली मणियोंद्वारा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8252)
- **Original**: बैठे हुए थे। महान्‌ बल-पराक्रमसे सम्पन्न भृगुवंशी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8253)
- **Original**: 386 कर संक्षिप्त श्रह्मवैवर्तपुराण + [[+[04(+(1+7+4]7+)4++0]4+]।) )
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8254)
- **Original**: 8 8 7 8] 3 888 808] परशुराम उन सबसे सम्भाषण करके हाथमें फरसा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8255)
- **Original**: आज्ञा लेकर यहाँ आता हूँ और तुम्हें साथ लिवा लिये हुए शीघ्र ही आगे बढ़नेको उद्यत हुए। उन्हें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8256)
- **Original**: ले चलूँगा। इस समय रुक जाओ ।' गणेशकी बात आगे बढ़ते देखकर गणेशने कहा--' भाई ! क्षणभर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8257)
- **Original**: सुनकर महाबली परशुराम, जो बृहस्पतिके समान ठहर जाओ। इस समय महादेव निद्राके वशीभूत
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8258)
- **Original**: वक्ता थे, कहनेके लिये उद्यत हुए। होकर शयन कर रहे हैं। मैं उन ईश्वरकी (अध्याय 41) परशुरामका शिवके अन्तःपुरमें जानेके लिये गणेशसे अनुरोध, गणेशका उन्हें समझाना, न माननेपर उन्हें स्तम्भित करके अपनी सूँड़में लपेटकर सभी लोकोंमें घुमाते हुए गोलोकमें श्रीकृष्णका दर्शन कराकर भूतलपर छोड़ देना, होशमें आनेपर परशुरामका कुपित होकर गणेशपर फरसेका प्रहार करना, गणेशका एक दाँत दूट जाना, देवलोकमें हाहाकार, पार्वतीका रुदन और शिवतसे प्रार्थना परशुरामने कहा--भाई! मैं ईश्वरको प्रणाम
- **Translation**: 

---

