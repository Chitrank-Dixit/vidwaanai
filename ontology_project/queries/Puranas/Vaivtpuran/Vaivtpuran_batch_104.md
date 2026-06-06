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

### Verse 1 (Vaivtpuran 7.9813)
- **Original**: रोहिणी देबीने आयी हुई स्त्रियोंको प्रसन्नतापूर्वक सुवर्णके सौ ढेर, चाँदी, धान्यकी पर्वतोपम राशि,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9814)
- **Original**: तैल, सिन्दूर और ताम्बूल प्रदान किये। वे सब वस्त्र, सहस्तरों मनोरम गौएँ, दही, दूध, शक्कर,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9815)
- **Original**: बालकके सिरपर आशीर्वाद दे अपने-अपने घरको माखन, घी, मधु, मिठाई, लड़ू, स्वादिष्ट मोदक,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9816)
- **Original**: चली गयीं। केवल यशोदा, रोहिणी और नन्द-ये सब प्रकारकी खेतीसे भरी-पूरी भूमि, वायुके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9817)
- **Original**: ही उस घरमें हर्षपूर्वक रहे। समान वेगशाली घोड़े, पान और तेल--इन सबका (अध्याय 9) सत्य 90-00
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9818)
- **Original**: डंडर + संक्षिप्त ब्रह्मवैवर्तपुराण * आकाशवाणी सुनकर कंसका पूतनाको गोकुलमें भेजना, पूतनाका श्रीकृष्णके मुखमें विषमिश्रित स्तन देना और प्राणोंसे हाथ धोकर श्रीकृष्णकी कृपासे माताकी गतिको प्राप्त हो गोलोकमें जाना भगवान्‌ नारायण कहते हैं--नारद! एक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9819)
- **Original**: और सब प्रकारका रूप धारण करनेमें समर्थ हो। दिन राजसभामें स्वर्णसिंहासनपर बैठे हुए कंसको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9820)
- **Original**: . नारद! ऐसा कहकर महाराज कंस उस बड़ी मधुर आकाशवाणी सुनायी दी--' ओ महामूढ़
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9821)
- **Original**: राजसभामें चुप हो रहा। इधर स्वेच्छाचारिणी नरेश! क्‍या कर रहा है? अपने कल्याणका उपाय
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9822)
- **Original**: पूतना कंसको प्रणाम करके वहाँसे चल दी। उसने सोच। तेरा काल धरतीपर उत्पन्न हो चुका है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9823)
- **Original**: परम सुन्दरी नारीका रूप धारण कर लिया। वसुदेवने मायासे तेरे शत्रुभूत बालककों नन्दके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9824)
- **Original**: उसकी अज्जकान्ति तपाये हुए सुवर्णके समान हाथमें दे दिया और उनकी कन्या लाकर तुझे सौंप
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9825)
- **Original**: प्रकाशित हो रही थी। वह अनेक प्रकारके दी। यह कन्या मायाका अंश है और वसुदेवके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9826)
- **Original**: आभूषणोंसे विभूषित थी और मस्तकपर मालतीकी पुत्रके रूपमें साक्षात्‌ श्रीहरि अवतीर्ण हुए हैं। वे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9827)
- **Original**: मालासे अलंकृत केशपाश धारण किये हुए थी। ही तेरे प्राणहन्ता हैं। इस समय गोकुलके नन्द-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9828)
- **Original**: उसके ललारमें कस्तूरीकी बेंदीसे युक्त सिन्दूरकी मन्दिरमें उनका पालन-पोषण हो रहा है। देवकीका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9829)
- **Original**: रेखा शोभा पा रही थी। पैरोंमें मझेर और सातवाँ गर्भ भी स्खलित या मृत नहीं हुआ है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9830)
- **Original**: कटिभागमें करधनीकी मधुर झनकार फैल रही योगमायाने उस गर्भको रोहिणीके उदरमें स्थापित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9831)
- **Original**: थी। ब्रजमें पहुँचकर पूतनाने मनोहर नन्द-भवनपर कर दिया था। उस गर्भसे शेषके अंशभूत
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9832)
- **Original**: दृष्टिपात किया। वह दुर्लड्बडु्य एवं गहरी खाइयोंसे महाबली बलदेवजी प्रकट हुए हैं। श्रीकृष्ण और
- **Translation**: 

---

