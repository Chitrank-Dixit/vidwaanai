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

### Verse 1 (Bhagwat_Geeta 1.101)
- **Original**: दुर्बुद्धि दुर्योधनका युद्धमें हित चाहनेवाले जो- जो ये राजा लोग इस सेनामें आये हैं, इन युद्ध करनेवालोंको मैं देखूँगा
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 1.102)
- **Original**: सजञ्ञय उवाच एवमुक्तो हषीकेशों गुडाकेशेन भारत। सेनयोरु भयोर्म ध्ये स्थापयित्वा रथोत्तमम्‌
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 1.103)
- **Original**: * अध्याय 1*% 19 भीष्मद्रोणप्रमुखत: सर्वेषां च महीक्षिताम्‌। उवाच्र पार्थ पश्यैतान्समवेतान्कुरूनिति
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 1.104)
- **Original**: संजय बोले--हे धृतराष्ट्र ! अर्जुनद्वारा इस प्रकार कहे हुए महाराज श्रीकृष्णचद्धने दोनों सेनाओंके बीचमें भीष्म और द्रोणाचार्यके सामने तथा सम्पूर्ण राजाओंके सामने उत्तम रथको खड़ा करके इस प्रकार कहा कि हे पार्थ ! युद्धके लिये जुटे हुए इन कौरवोंको देख
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 1.105)
- **Original**: तत्रापश्यत्स्थितान्‌ पार्थ: पितृनथ पितामहान्‌। आचार्यान्मातुलान्भ्रातृन्पुत्रान्पौत्रान्सखींस्तथा
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 1.106)
- **Original**: श्रशुरान्सुहरदश्चेव सेनयोरु भयोरपि। इसके बाद प्ृथापुत्र अर्जुनने उन दोनों ही सेनाओंमें स्थित ताऊ-चाचोंको, दादों-परदादोंको, गुरुओंको, मामाओंको, भाइयोंको, पुत्रोंको, पौत्रोंको तथा मित्रोंको, ससुरोंको और सुहृदोंको भी देखा
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 1.107)
- **Original**: 26 और र27वेंका पूर्वार्ध
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 1.108)
- **Original**: तान्समीक्ष्य स कौन्तेय: सर्वान्बन्धूनवस्थितान्‌।
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 1.109)
- **Original**: । कृपया परयाविष्टो विषीदच्निदमब्नवीत्‌। उन उपस्थित सम्पूर्ण बन्धुओंको देखकर वे कुन्तीपुत्र अर्जुन अत्यन्त करुणासे युक्त होकर शोक करते हुए यह वचन बोले
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 1.110)
- **Original**: 27 वेंका उत्तरार्ध और 28 वेंका पूर्वार्ध
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 1.111)
- **Original**: 20 * श्रीमद्धगवद़्ीता * अर्जुन उवाच दृष्लेमं स्वजनं कृष्ण युयुत्सुं समुपस्थितम्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 1.112)
- **Original**: सीदन्ति मम गात्राणि मुखं च परिशुष्यति। वेपथुश्च शरीरे मे रोमहर्षश्वच जायते
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 1.113)
- **Original**: अर्जुन बोले-हे कृष्ण! युद्धक्षेत्रमें डटे हुए युद्धेके अभिलाषी इस स्वजनसमुदायकों देखकर मेरे अंग शिथिल हुए जा रहे हैं और मुख सूखा जा रहा है तथा मेरे शरीरमें कम्प एवं रोमाशञ्न हो रहा है
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 1.114)
- **Original**: 28 वेंका उत्तरार्ध और 29
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 1.115)
- **Original**: गाण्डीवं स्त्रंसते हस्तात्त्वक्नैव परिदह्मते। न च शक्रोम्यवस्थातुं भ्रमतीव च मे मन:
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 1.116)
- **Original**: हाथसे गाण्डीव धनुष गिर रहा है और त्वचा भी बहुत जल रही है तथा मेरा मन भ्रमित-सा हो रहा है; इसलिये मैं खड़ा रहनेको भी समर्थ नहीं हूँ
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 1.117)
- **Original**: निमित्तानि चर पश्यामि विपरीतानि केशव । न च श्रेयोडनुपश्यामि हत्वा स्वजनमाहवे
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 1.118)
- **Original**: हे केशव! मैं लक्षणोंकों भी विपरीत ही देख रहा हूँ तथा युद्धमें स्वजनसमुदायको मारकर कल्याण भी नहीं देखता
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 1.119)
- **Original**: नकाडुश्षे विजयं कृष्ण न च राज्यं सुखानि च । कि नो राज्येन गोविन्द कि भोगैजीवितेन वा
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 1.120)
- **Original**: * अध्याय 1*% 21 हे कृष्ण! मैं न तो विजय चाहता हूँ और न राज्य तथा सुखोंको ही। हे गोविन्द! हमें ऐसे राज्यसे क्या प्रयोजन है अथवा ऐसे भोगोंसे और जीवनसे भी क्‍या लाभ है ?
- **Translation**: 

---

