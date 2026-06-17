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

### Verse 1 (Vaivtpuran 28.4246)
- **Original**: बन्धनके कष्टमें पड़ा हुआ पुरुष एक महीनेतक दक्षिणायै स्वाहा।' सुधीजनोंको चाहिये कि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4247)
- **Original**: इसका श्रवण करके इन सबसे छूट जाता है, इसमें सर्बपूजिता इन भगबती दक्षिणाकी अर्चना भक्तिपूर्वक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4248)
- **Original**: कोई संशय नहीं है। उत्तम विधिके साथ करें। (अध्याय 42) मी) देवी षष्टीके ध्यान, पूजन, स्तोत्र तथा विशद महिमाका वर्णन नारदजीने कहा--प्रभो! भगवती “पष्ठी',
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4249)
- **Original**: प्रेम करते हैं। बालकोंको दीर्घायु बनाना तथा मड्जगलचण्डिका तथा देवी मनसा-ये देवियाँ [उनका भरण-पोषण एबं रक्षण करना इनका मूलप्रकृतिकी कला मानी गयी हैं। मैं अब इनके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4250)
- **Original**: स्वाभाविक गुण है। ये सिद्धियोगिनी देवी अपने प्राकट्यका प्रसड़़ यथार्थरूपसे सुनना चाहता हूँ। योगके प्रभावसे बच्चोंके पास सदा विराजमान भगवान्‌ नारायण कहते हैं--मुने! रहती हैं। ब्रह्मन्‌! इनकी पूजा-विधिके साथ ही मूलप्रकृतिके छठे अंशसे प्रकट होनेके कारण ये
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4251)
- **Original**: यह एक उत्तम इतिहास सुनो। पुत्र प्रदान *चष्ठी ' देवी कहलाती हैं । बालकोंकी ये अधिष्ठात्री
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4252)
- **Original**: करनेवाला यह परम सुखदायी उपाख्यान धर्मदेवके देवी हैं। इन्हें “विष्णुमाया' और 'बालदा' भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4253)
- **Original**: मुखसे मैंने सुना है। कहा जाता है। मातृकाओंमें 'देवसेना' नामसे ये प्रियव्रत नामसे प्रसिद्ध एक राजा हो चुके प्रसिद्ध हैं। उत्तम ब्रतका पालन करनेवाली इन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4254)
- **Original**: हैं। उनके पिताका नाम था--स्वायम्भुव मनु। साध्वी देवीको स्वामी कार्तिकेयकी पत्नी होनेका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4255)
- **Original**: प्रियव्रत योगिराज होनेके कारण विवाह करना सौभाग्य प्राप्त है। वे प्राणोंसे भी बढ़कर इनसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4256)
- **Original**: नहीं चाहते थे। तपस्यामें उनकी विशेष रुचि
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4257)
- **Original**: थी। परंतु ब्रह्माजीकी आज्ञा तथा सत्प्रयत्रके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4258)
- **Original**: विग्रह ग्रीष्मकालीन सूर्यके समान चमचमा रहा प्रभावसे उन्होंने बिबाह कर लिया। मुने!
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4259)
- **Original**: था। उन्हें प्रसन्न देखकर राजाने पूछा। विवाहके बाद सुदीर्घकालतक उन्हें कोई भी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4260)
- **Original**: राजा प्रियत्रतने पूछा--सुशोभने! कान्‍्ते! संतान नहीं हो सकी। तब कश्यपजीने उनसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4261)
- **Original**: सुव्रते! वरारोहे! तुम कौन हो, तुम्हारे पतिदेव पुत्रेष्टि-यज्ञ कराया। राजाकी प्रेयसी भार्याका नाम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4262)
- **Original**: कौन हैं और तुम किसकी कन्या हो? तुम मालिनी था। मुनिने उन्हें चरु प्रदान किया। चरु-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4263)
- **Original**: स्त्रियोंमें धन्यवाद एबं आदरकी पात्र हो। भक्षण करनेके पश्चात्‌ रानी मालिनी गर्भवती हो नारद! जगत्‌को मड्जल प्रदान करनेमें प्रवीण गयीं। तत्पश्चात्‌ सुवर्णके समान प्रतिभावाले एक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4264)
- **Original**: तथा देवताओंके रणमें सहायता पहुँचानेवाली वे कुमारकी उत्पत्ति हुई; परंतु सम्पूर्ण अद्ोंसे सम्पन्न
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4265)
- **Original**: भगवती 'देवसेना' थीं। पूर्वसमयमें देवता दैत्योंसे वह कुमार मरा हुआ था। उसकी आँखें उलट
- **Translation**: 

---

