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

### Verse 1 (Vaivtpuran 543.15994)
- **Original**: सुशोभित था। तदनन्तर रासमण्डलकी शोभा, मधुपर्क निवेदित किया। तदनन्तर वे पूछने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15995)
- **Original**: असंख्य गोपी तथा श्रीकृष्ण ही आ गये-इस लगॉ--'उद्धव! नन्‍्दजी कहाँ हैं? तथा बलराम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15996)
- **Original**: अनुमानसे असंख्य गोपोंको प्रतीक्षा करते देखा। और श्रीकृष्ण कहाँ हैं? वह सब वृत्तान्त ठीक-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15997)
- **Original**: फिर यमुनाकी प्रदक्षिणा करके उद्धवने चन्दन, ठीक बतलाओ।' तब उद्धवने क्रमशः: कहना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15998)
- **Original**: चम्पक, यूथिका, केतकी, माधवी, मौलसिरी, आरम्भ किया-'यशोदे! सुनो, वे सब सर्वथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15999)
- **Original**: अशोक, काझन, कर्णिका आदि बनोंकी प्रदक्षिणा सकुशल हैं; नन्दजी आनन्दपूर्वक हैं। वे श्रीकृष्ण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16000)
- **Original**: की। फिर आनन्दपूर्ण मनसे नागेश्वर, लवब्, और बलरामके साथ कुछ विलम्बसे आयेंगे;
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16001)
- **Original**: शाल, ताल, हिंताल, पनस, रसाल, मन्दार आदि क्योंकि वहाँ श्रीकृष्णेके उपनयन-संस्कारतक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16002)
- **Original**: काननोंको देखते हुए रमणीय कुझवनके दर्शन ठहरेंगे। मैं विधिपूर्वक तुम लोगोंका कुशल-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16003)
- **Original**: करके अत्यन्त मधुर रमणीय मधुकाननमें प्रवेश समाचार जानकर मथुरा लौट जाऊँगा।' इस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16004)
- **Original**: किया। पुन: बदरीौवनमें जानेके बाद कदलीवनमें मड्रल-समाचारकों सुनकर यशोदा और रोहिणी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16005)
- **Original**: जाकर अति निभृत स्थानमें श्रीराधिकाके आश्रमके आनन्दविभोर हो गयी; उन्होंने ब्राह्मणकों बुलाकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16006)
- **Original**: दर्शन किये। वहाँकी दिव्य विलक्षण शोभाकों रतन, सुवर्ण और उत्तम वस्त्र प्रदान किया। देखनेके बाद वे अन्तिम द्वार॒पर पहुँचे। सखियोंने तत्पश्चात्‌ उद्धवको अमृतोषम मिष्टान्न भोजन उनका स्वागत करके उन्हें राधाके पास पहुँचा कराया तथा उन्हें उत्तम मणि, रत्न और हीरे दिया। उद्धवने आश्चर्यचकित कर देनेवाली भेंटमें दिये। फिर नाना प्रकारके माड्लिक बाजे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16007)
- **Original**: राधाकों सामने देखा। बे चन्द्रकलाके समान बजवाये, मड्भल-कार्य कराया, ब्राह्मणोंकों जिमाया
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16008)
- **Original**: सुन्दरी थीं, उनके नेत्र पूर्णतया खिले हुए कमलके और वेदपाठ करवाया। फिर परमानन्दपूर्वक नाना
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16009)
- **Original**: सदृश थे, उन्होंने भूषणोंका त्याग कर दिया था, प्रकारके उपहार, नैवेद्य, पुष्प, धूप, दीप, चन्दन,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16010)
- **Original**: केवल कानोंमें सुबर्णके रंग-बिरंगे कुण्डल वस्त्र, ताम्बूल, मधु, गो-दुग्ध, दधि और घृत
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16011)
- **Original**: झलमला रहे थे, अत्यन्त क्लेशके कारण उनका आदि सामग्रियोंसे ब्राह्मणद्वारा सर्वव्यापी भगवान्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16012)
- **Original**: मुख लाल हो गया था, बे शोकसे मूच्छित हो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16013)
- **Original**: + श्रीकृष्णजन्मखण्ड * 699 भूमिपर पड़ी हुई रो रही थीं, उनको चेशाएँ शान्त
- **Translation**: 

---

