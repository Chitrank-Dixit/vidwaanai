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

### Verse 1 (Vaivtpuran 119.19090)
- **Original**: 39 हरये नम इति पृष्ठ पाद॑ सदावतु । 37 गोवर्धनधारिणे स्वाहा सर्वशरीरकम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 119.19091)
- **Original**: प्राच्यां मां पातु श्रीकृष्ण आग्नेय्यां पातु माधव: । दक्षिणे पातु गोपीशो नैक़्त्यां नन्दनन्दनः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 119.19092)
- **Original**: वारुण्यां पातु गोविन्दो वायव्यां राधिकेश्वर:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 119.19093)
- **Original**: उत्ते पातु रासेश ऐशान्यामच्युत: स्वयम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 123.19321)
- **Original**: » श्रीराथास्तोत्राणि » <39 युवयो; पादपओं च॒ दुर्लभ॑ प्राप्य पुण्यवान्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 123.19322)
- **Original**: क्षणार्ध घोड़शांशं च न हि मुझलति दैवत:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 123.19323)
- **Original**: भ्रक्‍त्या च॒ युवयोर्मनत्र गृहीत्वा वैष्णवादपि। स्तर्व॑ या कवच यापि कर्ममूलनिकृन्तनम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 123.19324)
- **Original**: यो जपेत्‌ परया भक्त्या पुण्यक्षेत्रे चः भारते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 123.19325)
- **Original**: पुरुषाणां सहस््र॑ च॒स्वात्मना सार्श्मुद्धरेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 123.19326)
- **Original**: गुरुमभ्यर््यय विधिवद्‌_ वस्त्रालंकारचन्दनै: । कवच धारयेद्‌ यो हि विष्णुतुल्यो भवेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 123.19327)
- **Original**: इति अजक्रह्मवैवर्ते गणेशकृतं श्रीराध्षास्तवन सम्पूर्णम्‌ / ( श्रीकृष्णजन्मखण्ड 123। 3-20) हट जटजम 40 220/-00000 बहोशशेषादिकृतं अश्रीराधास्तोत्रम्‌ ब्रह्मोवाच यष्टिवर्षसहस्राणि. दिव्यानि परमेश्वरि-+-पुष्के चर तपस्तसं पुण्यक्षेत्रे च भारते
- **Translation**: 

---

### Verse 12 (Vaivtpuran 123.19328)
- **Original**: त्वत्पादपद्ममधुरमथुलुब्धेन चेतसा । मधुत्रतेन लोभेन प्रेरितेते मया सति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 123.19329)
- **Original**: तथापि न मया लब्धं त्वत्यादपदमीप्सितम्‌ ।न दृष्टमपि स्वप्रेषपि जाता खागशरीरिणी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 123.19330)
- **Original**: वाराहे भारते वर्षे पुण्ये वृन्दावने बने । सिद्धाभ्रमे गणेशस्थ पादपडांं च॒ द्रक्ष्यसि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 123.19331)
- **Original**: राधामाथवयोदास्यं कुतो विषयिणस्तव । निवर्तस्व॒ महाभाग परमेतत्‌_ सुददुर्लभम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 123.19332)
- **Original**: इति श्रुत्था निवृत्तोडह॑ तपसे भग्नमानस: । परिपूर्ण तदधुना वाउिछतं तपसः फलम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 123.19333)
- **Original**: श्रीमहादेव उवाच पद: पद्मार्चित पादपद्यं यस्थ सुदुर्लभम्‌। ध्यायन्ते ध्याननिष्ठाश्ष शश्वद्‌ ब्रह्मादवः सुरा:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 123.19334)
- **Original**: मुनयो मनवश्चैव सिद्धा: सन्तश्ष योगिन:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 123.19335)
- **Original**: द्रष्ट नैव क्षमा: स्वप्ले भवती तस्य वक्षसि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 123.19336)
- **Original**: अनन्त उबाच वेदाश्न॒ बेदमाता च पुराणानि च सुत्रते। अहं सरस्वती सनन्‍्तः स्तोतुं चाल॑ च॒ संततम्‌
- **Translation**: 

---

