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

### Verse 1 (Vaivtpuran 15.6693)
- **Original**: पुष्पमाला, मछली और चन्दन-इन माम्नलिक भलीभाँति निर्माण किया था, उसमें स्थान-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6694)
- **Original**: वस्तुओंको, वामभागमें श्रृगाल, नकुल, कुम्भ और स्थानपर माणिक्य और हीरे जड़े गये थे, जिससे शुभदायक शवको तथा दक्षिणभागमें राजहंस,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6695)
- **Original**: * गणपतिखण्ड * 329 8 2285 8 ]]]]]]]][]]]][।[[[+7+]47+7
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6696)
- **Original**: मयूर, खञ्नन, शुक, कोकिल, कबूतर, शदह्लुचिल्ल (सफेद चील), माड्नलिक चक्रवाक, कृष्णसार- मृग, सुरभी और चमरी गौ, श्वेत चँंचर, सवत्सा धेनु और शुभ पताकाको देखा। उस समय नाना प्रकारके बाजोंकी मड्भलध्वनि सुनायी पड़ने लगी,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6697)
- **Original**: हरिकीर्तन तथा घण्टा और शह्बुका शब्द होने लगा। इस प्रकार मड्गनल-शकुनोंको देखते तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6698)
- **Original**: सुनते हुए कार्तिकेय आनन्दपूर्वक उस मनके समान बेगशाली रथके द्वारा क्षणमात्रमें ही पिताके मन्दिरपर जा पहुँचे। वहाँ कैलासपर पहुँचकर वे अविनाशी वट-वृक्षके नीचे कृत्तिकाओं तथा श्रेष्ठ पार्षदोॉके साथ कुछ देरके लिये ठहर गये। उस नगरके राजमार्ग बड़े मनोहर थे। उनपर चारों ओर पद्मराग और इन्द्रनीलमणि जड़ी हुई थी।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6699)
- **Original**: /““ समूह-के-समूह केलेके खंभे गड़े थे, जिनपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6700)
- **Original**: हर्षगढ़द हो गये। उस समय वे तुरंत ही रथसे रेशमी सूतमें गुँथे हुए चन्दनके पल्लबोंकी बन्दनवार
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6701)
- **Original**: उतर पड़े और सिर झुकाकर उन्हें प्रणाम करने लटक रही थी। वह पूर्ण कुम्भोंसे सुशोभित था।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6702)
- **Original**: लगे। तब पार्वतीने कार्तिकेयको देखकर लक्ष्मी उसपर चन्दनमिश्रित जलका छिड़काव किया गया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6703)
- **Original**: आदि देवियों, मुनि-पत्रियों और शिव आदि था। असंख्यों रत्रप्रदीषों तथा मणियोंसे उसकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6704)
- **Original**: सभीसे यत्रपूर्वक्ष परम भक्तिके साथ सम्भाषण विशेष शोभा हो रही थी। बह सदा उत्सवोंसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6705)
- **Original**: किया और उन्हें अपनी गोदमें उठाकर वे चूमने व्याप्त, हाथोंमें दूब और पुष्प लिये हुए वन्दियों
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6706)
- **Original**: लगीं। फिर शंकर, देवगण, पर्वत, शैलपत्रियों, और ब्राह्मणोंसे युक्त तथा पति-पुत्रवती साध्वी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6707)
- **Original**: पार्वती आदि देवियों तथा सभी मुनियोंने कार्तिकेयको नारियोंसे समन्वित था। समस्त मड्नल-कार्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6708)
- **Original**: शुभाशीर्वाद दिया। तदनन्तर कुमार गणोंके साथ करके पार्वती देवी लक्ष्मी, सरस्वती, दुर्गा, सावित्री, शिव-भवनमें आये। वहाँ सभाके मध्यमें उन्होंने तुलसी, रति, अरुन्धती, अहल्या, दिति, सुन्दरी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6709)
- **Original**: क्षीससागरमें शयन करनेवाले भगवान्‌ विष्णुको तारा, अदिति, शतरूपा, शची, संध्या, रोहिणी,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6710)
- **Original**: देखा। वे रज्नाभरणोंसे विभूषित हो रत्नसिंहासनपर अनसूया, स्वाहा, संज्ञा, वरुण-पत्नी, आकृति,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6711)
- **Original**: विराजमान थे। धर्म, ब्रह्मा, इन्द्र, चन्द्रमा, सूर्य, प्रसूति, देवहूति, मेनका, एक रंग तथा एक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6712)
- **Original**: अग्नि, बायु आदि देवता उन्हें घेरे हुए थे। उनका प्रकृतिवाली मैनाक-पत्नी, वसुन्धरा और मनसादेवीको
- **Translation**: 

---

