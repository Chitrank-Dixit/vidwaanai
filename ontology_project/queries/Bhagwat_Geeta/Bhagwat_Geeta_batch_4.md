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

### Verse 1 (Bhagwat_Geeta 0.61)
- **Original**: संजय बोले--उस समय राजा दुर्योधनने व्यूहरचनायुक्त पाण्डवोंकी सेनाको देखकर और द्रोणाचार्यके पास जाकर यह वचन कहा
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 0.62)
- **Original**: पश्यैतां पाण्डुपुत्राणामाचार्य महतीं चमूम्‌। व्यूढां द्रुपदपुत्रेण तव शिष्येण धीमता
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 0.63)
- **Original**: हे आचार्य ! आपके बुद्धिमान्‌ शिष्य द्वुपदपुत्र धृष्टचुम्रद्वारा व्यूहाकार खड़ी की हुई पाण्डुपुत्रोंकी इस बड़ी भारी सेनाको देखिये
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 0.64)
- **Original**: श्ड * श्रीमद्धगवद्रीता * अन्न शूरा महेष्वासा भीमार्जुनसमा युधि। युयुधानो विराटश्वच द्रपदश्च॒ महारथः
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 0.65)
- **Original**: धृष्टकेतुश्नेकितान: काशिराजश्च वीर्यवान्‌। पुरुजित्कुन्तिभोजश्च शैब्यश्च नरपुड्गभवः
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 0.66)
- **Original**: युधामन्युश्च विक्रान्त उत्तमौजाश्व वीर्यवान्‌। सौभद्रो द्रौपदेयाश्व सर्व एवं महारथाः
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 0.67)
- **Original**: इस सेनामें बड़े-बड़े धनुषोंवाले तथा युद्धमें भीम और अर्जुनके समान शूरवीर सात्यकि और विराट तथा महारथी राजा द्वुपद, धृष्टकेतु और चेकितान तथा बलवान्‌ काशिराज, पुरुजितू, कुन्तिभोज और मजुष्योंमें श्रेष्ठ शैब्य, पराक्रमी युधामन्यु तथा बलवान्‌ उत्तमौजा, सुभद्रापुत्र अभिमन्यु एवं द्रौपदीके पाँचों पुत्र--ये सभी महारथी हैं
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 0.68)
- **Original**: अस्माकं तु विशिष्टा ये तान्निबोध द्विजोत्तम । नायका मम सैन्यस्य सज्ज्ञार्थ तान्‌ ब्रवीमि ते
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 0.69)
- **Original**: हे ब्राह्मणश्रेष्ठ ! अपने पक्षमें भी जो प्रधान हैं, उनको आप समझ लीजिये। आपकी जानकारीके लिये मेरी सेनाके जो-जो सेनापति हैं, उनको बतलाता हूँ
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 0.70)
- **Original**: भवान्‌ भीष्मश्च कर्णश्र॒ कृपश्च समितिञ्लय: । अश्वत्थामा विकर्णश्र सौमदत्तिस्तथेव च
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 1.71)
- **Original**: * अध्याय 1*% 17 आप-्रोणाचार्य और पितामह भीष्म तथा कर्ण और संग्रामविजयी कृपाचार्य तथा वैसे ही अश्वत्थामा, विकर्ण और सोमदत्तका पुत्र भूरिश्रवा
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 1.72)
- **Original**: अन्ये च बहव: शूरा मदर्थ त्यक्तजीविता: । नानाशस्त्रप्रहरणा: सर्वे युद्धविशारदा:
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 1.73)
- **Original**: और भी मेरे लिये जीवनकी आशा त्याग देनेवाले बहुत-से शूरवीर अनेक प्रकारके शस्त्रास्त्रोंसे सुसज्जित और सब-के-सब युद्धमें चतुर हैं
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 1.74)
- **Original**: अपर्याप्तं तदस्माकं बल॑ भीष्माभिरक्षितम्‌। पर्याप्त त्विदमेतेषां बल॑ भीमाभिरक्षितम्‌
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 1.75)
- **Original**: भीष्मपितामहद्वारा रक्षित हमारी वह सेना सब प्रकारसे अजेय है और भीमद्ठारा रक्षित इन लोगोंकी यह सेना जीतनेमें सुगम है
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 1.76)
- **Original**: अयनेषु चर सर्वेषु यथाभागमवस्थिता:। भीष्ममेवाभिरक्षन्तु भवन्तः सर्व एव हि
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 1.77)
- **Original**: इसलिये सब मोर्चोपर अपनी-अपनी जगह स्थित रहते हुए आपलोग सभी निःसन्देह भीष्मपितामहकी ही सब ओरसे रक्षा करें
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 1.78)
- **Original**: तस्य सञझ्जनयन्‌ हर्ष कुरुवृद्ध:ः पितामहः । सिंहनादं विनद्योच्चै: शट्धृं दध्मौ प्रतापवान्‌
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 1.79)
- **Original**: 16 * श्रीमद्धगवद्रीता * कौरवोंमें वृद्ध बड़े प्रतापी पितामह भीष्मने उस दुर्योधनके हृदयमें हर्ष उत्पन्न करते हुए उच्च स्वरसे सिंहकी दहाड़के समान गरजकर शंख बजाया
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 1.80)
- **Original**: ततः शद्डाश्व भे्यश्व॒ पणवानकगोमुखा: । सहसैवाभ्यहन्यन्त स शब्दस्तुमुलो5भवत्‌
- **Translation**: 

---

