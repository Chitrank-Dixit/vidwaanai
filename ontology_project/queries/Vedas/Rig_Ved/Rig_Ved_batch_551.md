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

### Verse 1 (Rig Ved 0.11001)
- **Original**: 4785, या त ऊतिरमित्रहन्मक्षृजवस्तमासति । तया नो हिनुही रथम्‌
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11002)
- **Original**: हे इद्धदेव !आप तीव्रगामी हैं । शत्रु को जीतने के लिए आप उसी वेग से हमारे रथ को चलने की प्रेरणा दें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11003)
- **Original**: 4786. स रथेन रथीतमो3स्माकेनाभियुग्वना
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11004)
- **Original**: जेषि जिष्णो हित॑ धनम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11005)
- **Original**: मं0 6 सु0 45 प्र हे इद्धदेव ! आप महारथी हैं । आप अपने शत्रुओं को जीतने वाले रथ से शत्रुओं को सम्पत्ति को जीते
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11006)
- **Original**: 4787 य एक कत्तमु प्टृहि कृष्टीनां विचर्षणि:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11007)
- **Original**: पतिर्जज्ञे वृषक्रतु:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11008)
- **Original**: जो इन्द्रदेव प्रजाओं के स्वामी हैं, बल से होने वाले कार्यों को करने वाले एवं सबको विशेष दृष्टि से देखन वाले हैं, उन इन््रदेव की स्तुति करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11009)
- **Original**: 4788, यो गृणतामिदासिथापिरूती शिव: सखा। स त्वं न इन्द्र मृठय
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11010)
- **Original**: है इद्धदेव ! आप सबकी रक्षा करने वाले मित्र रूप हैं। आप सुखदाता एवं स्तोताओं के बन्धु सदृश हैं । आप हमें सुख प्रदान करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11011)
- **Original**: 4789. धिष्य बच्र॑ ग्स्त्यो रक्षोहत्याय वजच्रिव:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11012)
- **Original**: सासहीष्ठा अभि स्पृथ:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11013)
- **Original**: है वज़रधारी इन्द्रदेव ! आप असुरों का संहार करने के लिए वज्ञ को धारण करें और स्पर्धा करने वाले शत्रुओं को पराजित करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11014)
- **Original**: 4790, प्रल॑ रयीणां युजं सखाय॑ कीरिचोदनम्‌। ब्रह्मवाहस्तमं हुवे
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11015)
- **Original**: जो इन्द्रदेव मित्ररूपु स्तुति करने वालों के प्रेरक, धन देने बाले एवं आबाहन करते येएय हैं । हम उन इन्धदेव का आवाहन करते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11016)
- **Original**: 4791. स हि विश्वानि पार्थिवाँ एको वबसूनि पत्यते
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11017)
- **Original**: गिर्वणस्तमो अ श्विगु:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11018)
- **Original**: जो इन्द्रदेव अतिशय स्तुत्य एवं तीवगामो हैं, वे इन्रदेव समस्त पार्थिव धनों के एक मात्र स्वामी हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11019)
- **Original**: 4792. स नो नियुद्धिरा पृण काम॑ वाजेभिरश्विभि:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11020)
- **Original**: गोमद्धिगोंपते धृषत्‌
- **Translation**: 

---

