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

### Verse 1 (Vishnu Puran 0.5101)
- **Original**: 1 आराधिताध्च_गोविन्दादाराधनपरैनरे: । यत्याप्यते फल श्रोतुं तच्चेच्छामि महामुने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5102)
- **Original**: 2 औपराइर उवाच यत्पृष्छति भव्रानेतत्सगरेण महात्मना । ओर्बष: ज्राह यथा पृष्टस्तन्पे निगदतइश्ूणु
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5103)
- **Original**: 3 सगरः प्रणिपत्वैनमौर्य पप्रच्छ भार्गवम्‌। विष्णोराराधनोपायसम्बन्ध॑ मुनिसत्तम
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5104)
- **Original**: 4 फल चाराधिते विष्णो यत्पुंसामभिजायते । स चाह पृष्टो यत्रेन तस्मै तन्मेडखिलं श्रूणु
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5105)
- **Original**: 5 ऑर्व उवाच भौम॑ सनोरथ स्वर्ग स्वर्गे रम्ये जे यरत्पदम्‌। अप्नोत्याराधिते किष्णों निर्वाणमपि चोत्तमम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5106)
- **Original**: 6 पल तेज़ पूरे जपमनाि की यावश -
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5107)
- **Original**: 79 यत्तु पृष्छसि भूषपाल कथमाराध्यते हरि: । तदहं सकले तुभ्यं कथयामि निवोध मे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5108)
- **Original**: 8 कलम जल आजलतेफ्करक पुरुषेण पर: पन्धा 4$
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5109)
- **Original**: 9 यजन्यज्ञान्यजत्येनें जपत्येने जपन्नप । मिप्नन्नन्यानिनस्थेन सर्वभूतो बतो हरि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5110)
- **Original**: 10 श्रीमैत्रेयजी खोल्ले--हे भगवन्‌ ! जो छोण संसास्को जीतना चाहते हैं वे जिस प्रकार जगत्पति भगवान्‌ विष्णुकी उपासना करते हैं, वह वर्णन क्ीजिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5111)
- **Original**: और हे महामुने ! उन गोबिन्दकी आराधना करनेपर आराघन- परायण पुरुषोंको जो फल मिलता है, यह भी मैं सुनना चाहता हूँ 2
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5112)
- **Original**: श्रीपराशरजी बोले--हे मैत्रेय ! तुम जो कुछ पूछते हो यहों बात महात्पा सगरने ओर्वसे पूछी थी। उसके उत्तरमें उन्होंने जो कुछ कहा यह मैं तुमको सुनाता हूँ, श्रवण करो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5113)
- **Original**: हे मुनिश्रेष्ठ ! सगरने भृगुवंज्ञी महात्मा और्वको प्रणाम करके उनसे भगवान्‌ विष्णुकी आराधनाके उपाय और विष्ण॒को उपासना करनेसे मनुष्यक्त्रे जो फल मिलता है उसके जिषयमें पूछा था । उनके पूछनेपर और्वने यन्रपूर्वक जो कुछ कहा था वह सब सुनो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5114)
- **Original**: और्च बोले--भगलवान्‌ विष्णुकी आराधना करनेसे मनुष्य भूमण्डल-सम्बन्धी समस्त मनोरथ, स्वर्ग, स्वर्गसे भी श्रेष्ठ बरद्यपद और परम निर्वाण-पद भी प्राप्त कर छेता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5115)
- **Original**: हे राजेन्द्र! वह जिस-जिस फर्की जितनी-जितनी इच्छछा करता है, अल्प हो या अधिक, श्रीअच्युतकी आग्रधनासे निश्चय ही यह सब प्र/( कर लेता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5116)
- **Original**: और हे भूपाल ! तुमने जो फूझ कि हरिकी आराधना किस प्रकार की जाय, सो सब मैं तुमसे कहता हैँ, सावधान होकर सुनो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5117)
- **Original**: जो पुरुष वर्ण श्रम-घर्मका पालन करनेवात्त्र है वही परमपुरुष विष्णुकी आराधना कर सकता है; उनको सन्तुष्ट करनेका ओर कोई मार्ग नहीं है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5118)
- **Original**: है नृप ! यज्ञॉका यजन करनेवाला पुरुष उन (कि्णु) हीका यजन करता है, जप करनेवाला उन्होंका जप करता है और दूसरोंकी हिसा करनेवात्शा उन्हींकी हिंसा करता है; क्योंकि भगवान्‌ हरि सर्वभूतमय हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5119)
- **Original**: 184 श्रीविष्णुपुराण (आ0 8 तस्मात्सदाचारवता पुरुषेण जनार्दन: । आराध्यते_ खबर्णोक्तिधर्मानुझ्ठानकारिणा ब्राह्मण: क्षत्रियो बैद्यः शुद्रश्न पृथिवीपते । स्वथर्मतत्परो विष्णुमाराधयति नान्यथा नान्यथा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5120)
- **Original**: 12 पैशुन्यमनृत॑ च न भाषते
- **Translation**: 

---

