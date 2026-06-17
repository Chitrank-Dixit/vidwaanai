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

### Verse 1 (Vaivtpuran 12.6474)
- **Original**: हेतु दूर्वा, अक्षत, पुष्प और चन्दनसे युक्त गये। पुनः सनातन श्रीहरिने उन मुनियोंकों
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6475)
- **Original**: पुष्ककका जल लाकर दिया। रज्नपात्रमें रखे हुए
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6476)
- **Original**: 322 « संक्षिप्त ब्रह्मवैवर्तपुरण * #ऋ#%#%##%##ऋ#ऋऋऊऋऊऋऋऊऋक कक ## 8 8 ####ऋ$ऋऋशऋऋ कक #%# 8 8 # 8 अक्ऋऋश् 4 44 4 # #
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6477)
- **Original**: कऋ# ह 85% क अंक शकरयुक्त द्रवका मधुपर्क प्रदान किया। पुनः --इसी मन्त्रसे भक्तिपूर्वक वस्तुएँ समर्पित स्वर्गलोकके वैद्य अश्विनीकुमारद्वारा निर्मित करके परमानन्दमें मग्र थे। इस मन्त्रमें बत्तीस स्रानोपयोगी विष्णुतैल, बहुमूल्य रत्नोंके बने हुए
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6478)
- **Original**: अक्षर हैं। यह सम्पूर्ण कामनाओंका दाता, धर्म, सुन्दर आभूषण, पारिजातके पुष्पोंकी सौ मालाएँ,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6479)
- **Original**: अर्थ, काम, मोक्षका फल देनेवाला और सर्वसिद्धिप्रद मालती, चम्पक आदि अनेक प्रकारके पुष्प, है। इसके पाँच लाख जपसे ही जापकको तुलसीके अतिरिक्त पूजोपयोगी तरह-तरहके पत्र,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6480)
- **Original**: मन्त्रसिद्धि प्राप्त हो जाती है। भारतवर्षमें जिसे चन्दन, अगुरु, कस्तूरी, कुंकुम, ढेर-के-ढेर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6481)
- **Original**: मन्त्रसिद्धि हो जाती है, वह विष्णु-तुल्य हो जाता रत्रप्रदीप और धूप सादर समर्पित किये। तत्पश्चात्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6482)
- **Original**: है। उसके नाम-स्मरणसे सारे विष्न भाग जाते हैं। उसे प्रिय लगनेवाले नैवेद्यों--तिलके लडू, जौ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6483)
- **Original**: निश्चय ही वह महान्‌ वक्ता, महासिद्ध, सम्पूर्ण और गेहूँके चूर्ण, पूड़ी, अत्यन्त स्वादिष्ट तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6484)
- **Original**: सिद्धियोंसे सम्पन्न, श्रेष्ठ कवियोंमें भी श्रेष्ठ गुणवान्‌, मनोहर पक्‍वान्न, शर्करामिश्रित स्वादिष्ट स्वस्तिकके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6485)
- **Original**: विद्वानोंके गुरुका गुरु तथा जगत्‌के लिये साक्षात्‌ आकारका बना हुआ त्रिकोण पकवानविशेष,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6486)
- **Original**: वाक्पति हो जाता है। उस उत्सवके अवसरपर गुड़युक्त खील, चिउड़ा और अगहनीके चावलके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6487)
- **Original**: आनन्दमग्र हुए देवताओंने इस मन्त्रसे शिशुकी आटेके बने हुए पदार्थके नानाप्रकारके व्यञ्ञनोंके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6488)
- **Original**: पूजा करके अनेक प्रकारके बाजे बजवाये, उत्सव साथ पहाड़ लगा दिया। नारद! फिर उस पूजनमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6489)
- **Original**: कराया, ब्राह्मणोंकों भोजनसे तृप्त किया; फिर उन सुन्दरी पार्वतीने हर्षमें भरकर एक लाख घड़े,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6490)
- **Original**: ब्राह्मणॉंको तथा विशेषतया वन्दियोंकों दान दिया। दूध, एक लाख घड़े दही, तीन लाख घड़े मधु श्रीनारायणजी कहते हैं--नारद! तदनन्तर और पाँच लाख घड़े घी सादर अर्पित किया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6491)
- **Original**: उस सभाके बीच विष्णु परमभक्तिपूर्वक सम्पूर्ण नारद! फिर अनार और बेलके असंख्य फल,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6492)
- **Original**: विष्नोंके विनाशक उन गणेश्वरकी भलीभाँति पूजा भाँति-भाँतिके खजूर, कैथ, जामुन, आम, कटहल,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6493)
- **Original**: करके उनकी स्तुति करने लगे। केला और नारियलके असंख्य फल दिये। इनके भ्रीविष्णुने कहा--ईश! मैं सनातन सिवा और भी जो ऋतुके अनुसार विभिन्न देशोंमें
- **Translation**: 

---

