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

### Verse 1 (Vishnu Puran 0.3081)
- **Original**: 39 भारता: केतुमालाश्र भद्गाश्वा: कुरवस्तथा । प्रत्राणि छोकपड्ास्य मर्यादाशैलबाह्मत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3082)
- **Original**: 40 बीचमें इत्त्रवृतयर्ष है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3083)
- **Original**: इसी प्रकार उसके पूर्वकी ओर चैत्ररथ, दक्षिणकी ओर गन्धमादन, पश्चिमक्त्रे ओर वैध्राज और उत्तरकी ओर नन्‍दन नामक बन है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3084)
- **Original**: तथा सर्वदा देवताओंसे सेवनीय अरुणोद, महाभद्र, असितोद और मानस---ये चार सरोवर हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3085)
- **Original**: हे मैत्रेय ! शीताम्भ, कुमुन्द, कुररी, माल्यवान,तंथा चैकेक आदि पर्वत [भुफ्यकी कर्णिकारूप] मेस्के पूर्ष- दिदाके फेसराचल हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3086)
- **Original**: त्रिकूट, शितिर, पतड़ें, रुचक और निषाद आदि केसराचल उसके दक्षिण और हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3087)
- **Original**: शिखिनासा, बेडूर्य, कपिल, गन्धमादन और जारुधि आदि उसके पक्चिमीय केसरपर्वत हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3088)
- **Original**: तथा. मेस्के अति समीपस्थ इलायृतवर्षमें और जठरादि देशॉमें स्थित शल्बल॒कूट, ऋषभ, हंस, नाग तथा काल्ख आदि पर्वत उत्तरदिज्ञाके केसराचल हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3089)
- **Original**: है मैत्रेय ! मेरके ऊपर अन्तरिक्षमें चौदह सहस्र योजनके विस्तारवाली ब्रह्माजीकी महापुरी (अह्मपुरी) है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3090)
- **Original**: उसके सब ओर दिल्ञा एवं निदिशाओंमें इन्द्रादि ल्ोेकपालॉंके आठ अति स्मणीक और विख्यात नगर हैं। 32
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3091)
- **Original**: विष्णुपादोद्धला श्रोगज्ञजो चन्द्रमण्डलक्ये चारों ओरसे आप्लावित कर -स्वर्गछोकसे बहापुरीमें शिरतो हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3092)
- **Original**: वहाँ गिरनेपर वे चारों दिश्ञाओंमें क्रमसे सीता, अलकनन्दा, चक्षु और भद्गा नामसे चार भागोंमें विभक्त हो जाती हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3093)
- **Original**: उनमेंसे सीता पूर्वकी ओर आकाश- मार्गसे एक पर्वतसे दूसरे पर्वतपर जाती हुई अत्तमें पूर्वस्थित भद्राश्नवर्षकों पास्कर समुद्रमें मिल जातो है। 35
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3094)
- **Original**: इसी प्रकार, है महामुने!। अलकननदा दक्षिण-दिशाकी ओर भारतवर्षमें आती है और सात भागोंमें विभक्त होकर समुद्रमें मिल जाती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3095)
- **Original**: चक्षु पत्चिमदिशाके समस्त पर्वतोंको पास्कर केतुमाक नामक चर्षमें बहती हुई अन्तमें सागरमें जा गिरती है । 37
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3096)
- **Original**: तथा है महामुने ! भद्गा उत्तरके पर्वतों और उत्तरकुरुवर्षको पार करती हुई उत्तरीय समुद्रमें पिछ जातों है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3097)
- **Original**: माल्यवान्‌ और गख्धमादनपर्वत उत्तर तथा दक्षिणक्तरी ओर नीलाचल और निषधपर्वत्तक फैले हुए हैं। उन दोनोंके बीचों कर्णिक्मरकार मेरुपर्बत स्थित है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3098)
- **Original**: है मैश्रेय ! मर्यादापर्वतोंके बहिर्भागमें स्थित भारत, केतुमाल, भद्गाश्न और कुरुवर्ष इस स्प्रेकपद्मके फ्तॉके
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3099)
- **Original**: आण्रे ] द्वितीय अंझ 111 जठरों देबकूटश्ल मर्यादापर्वताबुभौ । तो दक्षिणोत्तरायामावानीरूनिषधायतौ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3100)
- **Original**: 49 पन्यमादनकसाली... पर्णप्शाप्ताइफ पूर्वपः ।
- **Translation**: 

---

