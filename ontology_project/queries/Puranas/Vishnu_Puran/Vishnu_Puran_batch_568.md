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

### Verse 1 (Vishnu Puran 0.11341)
- **Original**: तब भगवान्‌ मधुसूदनने 'अच्छा, मैंने क्षमा की' ऐसा कहकर उस वैष्णव ज्वरको अपनेमें लीन कर लिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11342)
- **Original**: ज्वर खोल्ला--जो मनुष्य आपके साथ मेरे इस युद्धका स्मरण करेंगे वे ज्वरहीन हो जायैंगे ऐसा कहकर बह चला गया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11343)
- **Original**: तदनन्तर भगवान्‌ कृष्णचद्धने पद्माम्रियॉँंकों जीतकर नष्ट किया और फिर स्जैक्मसे ही दानवसेनाको नष्ट करने लगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11344)
- **Original**: तब सम्पूर्ण दैत्यसेनाके सहित अलि-पुत्र बाणासुर, भगवान्‌ पार और स्वामिकार्त्तिकेयजी भगवान्‌ कृष्णके साथ युद्ध करने लगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11345)
- **Original**: श्रीहरि और श्रीमहादेवजोका परस्पर बड़ा घोर युद्ध हुआ, इस युद्धमें प्रयुक्त शस्तरास्“ोंके किरणजालसे सनन्‍्तप्त होकर सम्पूर्ण ल्तेक क्षुब्ध हो गये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11346)
- **Original**: इस घोर युद्धके उपस्थित होनेपर देवताओंने समझा कि निश्चय ही यह सम्पूर्ण जगत्‌का प्र्यकाल आ गया है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11347)
- **Original**: श्रीगोविन्दने जृष्भकान्न छोड़ा जिससे महादेवजी निद्वित-से होकर जमुहाई लेने लगे; उनकी ऐसी दद्गा देखकर दैत्य और प्रमथगण चारों ओर भागने लगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11348)
- **Original**: भगवान्‌ शक्कर निद्राभिभूत होकर रथके पिछले भागमें बैठ गये और फिर अनायास ही अद्भुत कर्म करनेवाले श्रीकृष्णचन्द्रसे युद्ध न कर सके
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11349)
- **Original**: तदनन्तर गरुडद्वारा वाहनके नष्ट हो जानेसे, प्रद्युप्रजीके शख्मेंसे पीड़ित होनेसे तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11350)
- **Original**: डै00 जृम्मिते शड्डरे नष्टे दैत्यसैन्ये गुह्टे जिते। नीते प्रमथ्सैन्ये च सद्लृयं शार्ड्धन्बना
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11351)
- **Original**: 27 आाण्यय चोद कृष्णकाब्िब्ेसए। योदुं कृष्णकार्ष्णिबलैस्सह
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11352)
- **Original**: 28 बलभद्रो महावीयों बाणसैन्यमनेकधा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11353)
- **Original**: विव्याध बाणै: प्रश्नइय धर्मतश्चन पछायत
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11354)
- **Original**: 29 आकृष्य लाजुलाग्रेण मुसलेनाशु ताडितम्‌ । बलें बलेन ददूशे बाणो बाणैश्व चक्रिणा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11355)
- **Original**: 30 ततः कृष्णेन बाणस्य बुद्धमासीत्सुदारुणम्‌ । समस्यतोरिषून्दीप्तान्कायत्राणविभेदिन:.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11356)
- **Original**: 31 कृष्णश्निच्छेद बाणैस्तान्वाणेन प्रहिताब्छितानू। विव्याध केशवं बाणो बाण विव्याध चक्रधूक्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11357)
- **Original**: 32 मुमुचाते तथासत्राणि बाणकृष्णौ जिगीषया । परस्पर क्षतिकराौ लाघवादनिर्श द्विज
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11358)
- **Original**: 33 भिद्ममानेष्रृशेषेषु झरेघप्रृख्के ले सीदति। प्राचुयेण ततो बार्ण हन्तुँ चक्रे हरिमन:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11359)
- **Original**: 34 ततो3र्कशतसझ्लततेजसा. सदृशद्युति । जग्राह दैत्यच्क्रारिहरिश्॒क्॑ सुदर्शनम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11360)
- **Original**: 35 मुझतो बाणनाशाय ततश्नक्रे मधुद्विष:। नप्ना पुरतो हरे:
- **Translation**: 

---

