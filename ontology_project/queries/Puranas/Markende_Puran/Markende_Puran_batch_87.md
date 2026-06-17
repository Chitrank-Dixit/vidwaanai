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

### Verse 1 (Markende Puran 0.1721)
- **Original**: कामरूप नामक पर्वतक्ने ऊपर त्रिजय नामक्ला कुगर स्वीकार क्यें।' बसाया और उसे अपने पुत्र विजयके अंधिकारमें कल्लाचतोकी यह प्रार्थना सुनकर स्वरोचिषूने
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1722)
- **Original**: दे दिया। उत्तर दिशामें मेरूनन्‍दके लिये नन्‍्दवर्ती +एब्रमस्तु” कहा। विभावरी और कलावतीकी
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1723)
- **Original**: नामकी पुरी बनवादी, जिसको चहारदीवांरीं बहुत स्नेंहपूर्ण दृष्टिसे विवाहका अभ्ुपोदन पाकर उन्होंने
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1724)
- **Original**: ऊँची थीं। कलावतीके पुत्र प्रभावके लिये दक्षिण क्न दोनोंका पार्णिग्रहण किया। फिर आपनी तीनों
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1725)
- **Original**: देशमें उन्होंने ताल नामक नागर बसाया। इस पत्नियोंके साथ वे स्मणीव बनों तथा झरनोंसे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1726)
- **Original**: प्रकार तीन नगऐंपें तीनों पुत्नॉंको रखकर पुरुषश्रेष् सुशोभित मिरिराजके शिखरपर विहार करते लगे।
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1727)
- **Original**: स्वरोचिष्‌ अपनी पत्नियोंके साथ अत्यन्त मनोहर स्वग्नेचिघ्ने छः सौ वर्षोत्क उन स्त्रियोंके स्राथ
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1728)
- **Original**: प्रदेशोर्में क्रिहार करने लोगे। एक दिन बे हाथमें स्मण किया। थे धर्मका विशेध न करते हुए
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1729)
- **Original**: धनुष लिये वनमें घरूप रहे थे। उस समर्य उन्हें सम्पूर्ण धार्मिक क्रियाओंका अनुष्ठान करते और
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1730)
- **Original**: बहुत दृश्4पर एक सुआर दिखाती दिया। उसे विधयोंकों भी भोगतें थे। तदनन्तर स्वरोचिष्के
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1731)
- **Original**: देखकर उन्होंने धनुष खोंचा, इतनेपें ही एक विजय, पेंरुननद तथा महाबली प्रभात-ये तीन
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1732)
- **Original**: हरिणी उनके पास्त आकर बोली--'वीरवर! आप पुत्र हुए। इन्दीबरकी पुत्री पदोग्माने विजयकों
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1733)
- **Original**: कृपा करके मुझपर हो बाण मारिये। इस मुअरको जन्म दिया था, विभावरीके गर्भसे -मेरुनन्द. और
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1734)
- **Original**: मारनेसे क्या लाभ। सुझक्तो ही तुरंत मार गिराइये। [539 ] सं0 मा0 पु0--6&
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1735)
- **Original**: श्54ड »संश्षिप्त पार्कण्डेयपुराण * #&#& 55#6& & #&&& #&## ###4 4 # 844 & « # 44447 #:#। 4 4 + # +; # है: क हैते
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1736)
- **Original**: 5441 993993 57 749 कक क कक
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1737)
- **Original**: 2006 कक 4 आज ह जज हक 1803 क कक 1277 भ का था आपका चलाबा हुआ बाण मुझे समस्त दुःखोंसे मुक्त कर देंगा।' स्वरोचिषुने कहा--देति
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1738)
- **Original**: तू चल्लल कटक्षेबाली मृगी है और मैं मनुष्यरूपथारी जीव हूँ; फिर स्वरोचिघूने कह्टा --मुझे तेरे शरीरमें कोई रोग
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1739)
- **Original**: मेरे-जैसे पुरुषका तेरे साथ किस प्रकार संयोग नहों दिखायी देता; फिर क्‍या कारण है कि तू
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1740)
- **Original**: होगा? अमने प्राणोंकों त्याग देना चाहतो है? मृगी बलोल़ीं--जिस पुरुषमें मेरा चित्त लगा हुआ है, उसका मन दूसरी स्त्रियोंमें आसक्त है, अतः उसके बिना मेरी मृत्यु निश्चित है। ऐसी दशामें बराणोंकी चोट सहनेके खिला पेंरे लिये यहाँ दूसरी कौन-सी द्ववा है। स्वरोचिषने कहा-- भीरु
- **Translation**: 

---

