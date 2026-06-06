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

### Verse 1 (Vaivtpuran 543.13834)
- **Original**: प्रकारको है। कल्प भी अनेक हैं तथा ब्रह्माण्ड उन्हें आशीर्वाद दिया। इन्द्रने मधुपर्क आदि देकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13835)
- **Original**: भी कितने ही प्रकारके हैं। उन ब्रह्माण्डोंमें उनकी पूजा की और ब्राह्मणबालकसे पूछा-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13836)
- **Original**: अनेकानेक ब्रह्मा, विष्णु, महेश तथा इन्द्र भी “कहिये, किसलिये आपका शुभागमन हुआ है?
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13837)
- **Original**: बहुतेरे हैं। उन सबकी गणना कौन कर सकता इन्द्रका वचन सुनकर ब्राह्मणबालकने जो । है? सुरेश्वर! भूतलके धूलिकणोंकी गणना कर बृहस्पतिके गुरुके भी गुरु थे, मेघके समान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13838)
- **Original**: ली जाय तो भी इन्द्रोंकी गणना नहीं हो सकती गम्भीर वाणीमें कहा। है; ऐसा विद्वानोॉका मत है। इन्द्रकी आयु और ब्राह्मण बोले--देवेन्र ! मैंने सुना है कि
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13839)
- **Original**: अधिकार इकहत्तर चतुर्युगतक है। अद्टाईस तुम बड़े विचित्र और अद्भुत नगरका निर्माण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13840)
- **Original**: इन्द्रोंका पतन हो जानेपर विधाताका एक दिन- करा रहे हों; अत: इस नगरको देखने तथा इसके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13841)
- **Original**: रात पूरा होता है। इस तरह एक सौ आठ वर्षोंतक विषयमें मनोवाड्छत बातें पूछनेके लिये मैं यहाँ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13842)
- **Original**: ब्रह्माजीकी सम्पूर्ण आयु है। जहाँ बिधाताकी भी आया हूँ। कितने वर्षोतक इसका निर्माण कराते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13843)
- **Original**: संख्या नहीं है, वहाँ देवेन्द्रोंकी गणना कया हो रहनेके लिये तुमने संकल्प किया है? अथबवा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13844)
- **Original**: सकती है? जहाँ ब्रह्माण्डोंकी ही संख्या ज्ञात नहीं विश्वकर्मा कितने वर्षोंमें इसका निर्माणकार्य पूर्ण
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13845)
- **Original**: होती; वहाँ ब्रह्मा, विष्णु और महेशकी कहाँ कर देंगे? ऐसा निर्माण तो किसी भी इन्द्रने नहीं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13846)
- **Original**: गिनती है? महाविष्णुके रोमकूपजनित निर्मल किया था। ऐसे सुन्दर नगरके निर्माणमें दूसरा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13847)
- **Original**: जलमें ब्रह्माण्डकी स्थिति उसी तरह है, जैसे कोई विश्वकर्मा भी समर्थ नहीं है। सांसारिक नदी-नद आदिके जलमें कृत्रिम नौका ब्राह्मणबालककी यह बात सुनकर देवराज
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13848)
- **Original**: हुआ करती है। इस प्रकार महाविष्णुके शरीरमें इन्द्र हँसने लगे। वे सम्पत्तिक मदसे अत्यन्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13849)
- **Original**: जितने रोएँ हैं, उतने ब्रह्माण्ड हैं; अतएव ब्रह्माण्ड मतवाले हो रहे थे; अतः उन्होंने उस द्विजकुमारसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13850)
- **Original**: असंख्य कहे गये हैं। एक-एक त्रह्माण्डमें पुनः पूछा--' ब्रह्मन्‌! आपने कितने इन्द्रोंका समूह तुम्हारे-जैसे कितने ही देवता निवास करते हैं। देखा अथवा सुना है? तथा कितने प्रकाके. इसी बीचमें पुरुषोत्तम श्रीहरिने वहाँ चौंटोंके विश्वकर्मा आपके देखने या सुननेमें आये हैं? समूहकों देखा, जो सौ धनुषकी दुरीतक फैला
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13851)
- **Original**: + श्रीकृष्णजन्मखण्ड * 601 ऊश1%%4########## ####ऋऋ#ऋऋक कक ऋक््ऋऋ%%%ऊ$%#$%%$% कक 44% हुआ था। बारी-बारीसे उन सबकी ओर देखकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13852)
- **Original**: मृगचर्म, मस्तकपर जटा, ललाटमें उज्बवल वे ब्राह्मणबालकका रूप धरकर पधारे हुए
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13853)
- **Original**: तिलक, वक्ष:स्थलमेँ रोमचक्र तथा सिरपर चटाई भगवान्‌ उच्चस्वरसे हँसने लगे। किंतु कुछ बोले
- **Translation**: 

---

