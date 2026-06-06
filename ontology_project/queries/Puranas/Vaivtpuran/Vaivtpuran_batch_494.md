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

### Verse 1 (Vaivtpuran 28.4286)
- **Original**: अज्गहीन, अनेक पत्नियोंका स्वामी, भार्यारहित, दिया और बड़े आदरके साथ उनकी पूजा और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4287)
- **Original**: रूपवान्‌, रोगी और धर्मी होनेमें मुख्य कारण स्तुति की। नारद! उस समय स्कन्दकी प्रिया देवी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4288)
- **Original**: अपना कर्म ही है। कर्मके अनुसार ही व्याधि षष्ठी अपने तेजसे देदीप्यमान थीं। उनका शान्त
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4289)
- **Original**: होती है और पुरुष आरोग्यवान्‌ भी हो जाता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4290)
- **Original**: # प्रकृतिखण्ड « 235 न का या] ]]]घऋ!#4!288ो8हभ] न ध 82 858ाी2 8 240002(04444
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4291)
- **Original**: है। अतएव राजन्‌! कर्म सबसे बलवान्‌ है-यह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4292)
- **Original**: गुणी, शुद्ध, विद्वानोंका प्रेमभाजन तथा योगियों, बात श्रुतिमें कही गयी है। ज्ञानियों एवं तपस्वियोंका सिद्धरूप होगा। त्रिलोकीमें मुने! इस प्रकार कहकर देवी षष्ठीने उस
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4293)
- **Original**: इसकी कीर्ति फैल जायगी। यह सबको सब बालककों उठा लिया और अपने महान्‌ ज्ञानके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4294)
- **Original**: सम्पत्ति प्रदान कर सकेगा। प्रभावसे खेल-खेलमें ही उसे पुनः जीवित कर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4295)
- **Original**: . इस प्रकार कहनेके पश्चात्‌ भगवती देवसेनाने दिया। अब राजाने देखा तो सुवर्णके समान [उन्हें बह पुत्र दे दिया। राजा प्रियव्रतने पूजाकी प्रतिभावाला वह बालक हँस रहा था। अभी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4296)
- **Original**: सभी बातें स्वीकार कर लीं। यों भगवती महाराज प्रियत्रत उस बालककी ओर देख ही रहे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4297)
- **Original**: देवसेनाने उन्हें उत्तम बर दे स्वर्गके लिये प्रस्थान थे कि देवी देवसेना उस बालकको लेकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4298)
- **Original**: किया। राजा भी प्रसन्नमन होकर मन्त्रियोंके साथ आकाशमें जानेको तैयार हो गयीं। ब्रह्मन्‌! यह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4299)
- **Original**: अपने घर लौट आये। आकर पुत्रविषयक वृत्तान्त देख राजाके कण्ठ, ओष्ठ और तालू सूख गये,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4300)
- **Original**: सबसे कह सुनाया। नारद! यह प्रिय वचन सुनकर उन्होंने पुनः देवीकी स्तुति की। तब संतुष्ट हुई
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4301)
- **Original**: स्‍त्री और पुरुष सब-के-सब परम संतुष्ट हो गये। देवीने राजासे कर्मनिर्मित वेदोक्त वचन कहा।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4302)
- **Original**: राजाने सर्वत्र पुत्र-प्राप्तिकि उपलक्षमें माड्नलिक हा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4303)
- **Original**: कार्य आरम्भ करा दिया। भगवतीकी पूजा की। ब्राह्मणोंको बहुत-सा धन दान किया। तबसे 735 07)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4304)
- **Original**: प्रत्येक मासमें शुक्लपक्षकी षष्ठी तिथिके अवसरपर हि.
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4305)
- **Original**: भगवती षष्ठीका महोत्सव यत्रपूर्वक मनाया जाने 8 92 & है लगा। बालकोंके प्रसवगृहमें छठे दिन, इक्कीसवें 7% 0) 34 9: 23
- **Translation**: 

---

