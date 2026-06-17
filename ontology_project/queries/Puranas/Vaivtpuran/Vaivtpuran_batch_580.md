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

### Verse 1 (Vaivtpuran 45.4461)
- **Original**: सायंकाल होनेकों आया। सूर्यनारायण अस्ताचलको प्रसन्न हो गये। मुने! भगवान्‌ शंकरने प्रसन्न होकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4462)
- **Original**: जाने लगे। देवी मनसा परम साध्वी एवं पतित्रता इन्हें महान्‌ ज्ञान प्रदान किया। सामवेदका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4463)
- **Original**: थी। उसने मनमें विचार किया--' ट्विजोंके लिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4464)
- **Original**: + प्रकृतिखण्ड # रडरे कक ऋ्क्ऋ््््ऋ््ऋ्ऋऋ्ऋऋ्ऋझ# 44 44 # 4 4446 ### ######### कक कक कक नित्य सायंकाल संध्या करनेका विधान है। यदि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4465)
- **Original**: है--यह मेरा दोष अवश्य है। मेरे पति सोये ही रह जाते हैं तो इन्हें पाप इस प्रकार कहकर देवी मनसा भक्तिपूर्वक लग जायगा; क्योंकि ऐसा नियम है कि जो प्रात:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4466)
- **Original**: अपने स्वामी जरत्कारु मुनिके चरण-कमलोंमें और सायंकालकी संध्या ठीक समयपर नहीं
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4467)
- **Original**: पड़ गयीं। उस समय रोषके आवेशमें आकर करता, बह अपवित्र होकर पापका भागी होता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4468)
- **Original**: मुनि सूर्यको भी शाप देनेके लिये उद्यत हो गये। है।' यों विचार करके उस परम सुन्दरी मनसाने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4469)
- **Original**: नारद! उन्हें देखकर स्वयं भगवान्‌ सूर्य संध्यादेवीको पतिदेवको जगा दिया। मुने! मुनिवर जरत्कारु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4470)
- **Original**: साथ लेकर वहाँ आये और भयभीत होकर जगनेपर क्रोधसे भर गये। विनयपूर्वक मुनिवर जरत्कारुसे सम्यक्‌ प्रकारसे मुनिने कहा--साध्वि! मैं सुखपूर्वक सो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4471)
- **Original**: यथार्थ बात कहने लगे। रहा था; तुमने मेरी निद्रा क्यों भड् कर दी? भगवान्‌ सूर्यने कहा-- भगवन्‌! आप परम जो स्त्री अपने स्वामीका अपकार करती है, उसके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4472)
- **Original**: शक्तिशाली ब्राह्मण हैं। संध्याका समय देखकर श्रत, तपस्या, उपवास और दान आदि सभी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4473)
- **Original**: धर्मलोप हो जानेके भयसे इस साध्वीने आपको सत्कर्म व्यर्थ हो जाते हैं। स्वामीका अप्रिय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4474)
- **Original**: जगा दिया। मुने! विप्रवर! मैं आपकी शरणमें करनेवाली स्त्री किसी भी सत्कर्मका फल नहीं उपस्थित हूँ। मुझे शाप देना आपके लिये उचित प्राप्त कर सकती। जिसने अपने पतिकी पूजा की,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4475)
- **Original**: नहीं है। ब्राह्मणोंका हृदय सदा नवनीतके समान उससे मानो स्वयं भगवान्‌ श्रीकृष्ण सुपूजित हो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4476)
- **Original**: कोमल होता है। ब्राह्मण चाहें तो पुन: सृष्टि कर गये। पतिक्रताओंके ब्रतके लिये स्वयं भगवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4477)
- **Original**: सकते हैं; इनसे बढ़कर तेजस्वी दूसरा कोई है श्रीहरि पतिके रूपमें विराजमान रहते हैं। सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4478)
- **Original**: ही नहीं। ब्रह्मज्योति ब्राह्मणके द्वारा निरन्तर दान, यज्ञ, तीर्थसेवन, व्रत, तप, उपवास, धर्म,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4479)
- **Original**: सनातन भगवान्‌ श्रीकृष्णजी आराधना होती है। सत्य और देवपूजन-ये सब-के-सब स्वामीकी सूर्यके उपर्युक्त बचन सुनकर विप्रवर सेवाकी सोलहवीं कलाकी भी तुलना नहीं कर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4480)
- **Original**: जरत्कारु प्रसन्न हो गये। उनसे आशीर्वाद लेकर सकते। जो स्त्री भारतवर्ष-जैसे पुण्यक्षेत्रमें पतिकी
- **Translation**: 

---

