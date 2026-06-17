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

### Verse 1 (Markende Puran 0.3121)
- **Original**: स्र॒ ग्रपात महीपूछठे शस्त्रसज़ुसमाहतः'। जीरक्तश्न महीपाल रक्तवीजों महासूर:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3122)
- **Original**: ततस्ते हर्षभतुलमवापुस्त्रिशा नृपा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3123)
- **Original**: तेषां मातृगणो ज्ञातों ननर्तासृड्सदोद्धुत:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3124)
- **Original**: इस प्रकार क्रोधमें भरे हुए मात्तृगणोंको नाना प्रकारके उपायॉसे बद्धे-बड़े असुरोंका मर्दन करते देख दैत्यसैनिक्र भाग खड़े हुए
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3125)
- **Original**: मातृगणोंसे पीडित दैत्योंकों युद्धछों भागते देख रक्तबोज नामका महादँत्य क्रोधमें भरकर युद्धके लिये आया
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3126)
- **Original**: उसके शरीरसे जब रक्तको बूँद पृथ्चीपर गिरती, तय उसोके सपान शक्तिशाली एक दूसण महादैत्व पृथ्लोपर पैदा हो जाता #
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3127)
- **Original**: महासुर रक्तत्रीज़ हाथमें गदा लेकर उन्द्रशक्तिके साथ युद्ध करने लगा। तब ऐन्द्रीने अपने वज़से रक्तजीजकी मारोा
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3128)
- **Original**: बज़से जायल होनेपर उसके शरोरसे बहुत सा रक्त चुने लगा और उससे उसीके समान रूप तथा पराक्रमवाले योद्धा उत्पन्न होने लगे
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3129)
- **Original**: उसके शरीरसे रक्तकों जितनी बूँदें गिरी, उतने हो पुरुष उत्पन्न हो गये। वे सब रक्तबीजके समान ही जॉयंबान, बलवान्‌ जा पराक्रमी थे
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3130)
- **Original**: जे रकसे उत्पन्न होनेवाले युरुप भी अत्यन्त भयक्भुर अस्त्र-शस्वरोंका प्रह्मर करते हुए वहाँ मावृगणोंके साथ घोर युद्ध करने लगे #45
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3131)
- **Original**: यृत्रः वज्के प्रहाशले जब उसका मस्तक घायल हुआ तो रक्त बहने लगा और उससे हजारों पुरुष उत्पन्न हो गयग्ने
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3132)
- **Original**: वैष्णवीने युद्धमें रक्तत्रीजपर चक्रका प्रहार किया तथा ऐन्द्रीन, उस दैत्य-सेनापतिकों गदासे चोट पहुँचायी
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3133)
- **Original**: चैष्णओके चक्रसे घायल होनेपर उसके शरीरखे जो रक्त बहा और उससे जो डसोंके बराबर आकारवाले सहस्रों महारैत्य प्रकट व्वद कही ऋर्टी "ऋष्ल्टाव' इजना अधिक फढठ 3]
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3134)
- **Original**: र्र्र + संक्षिप्त मार्कण्डेयपुराण + हुए, उनके द्वाय सम्पूर्ण जगत्‌ ज्याप्त हों गया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3135)
- **Original**: कौमारोने शक्तिसे, वाराहोने खड़गसे और माह्तेश्वरीने जिशुलसे महादैत्य सक्तबीजकों घावल किया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3136)
- **Original**: क्रोध्पें भरे हुए ठस महादैत्य रक्तबीजने भी गदासे सभी माक्त- शक्तियीपर पृथक- पृथक प्रहार क्रिया
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3137)
- **Original**: शक्ति और शूल आदिसे अवेक बार घायल । होनेपर जो उसके शरोरसे रक्तकों धाग़ पृथ्वीपर गरी, उससे भी निश्चय हो सैकड़ों असर उत्पन्न हुए
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3138)
- **Original**: इस प्रकार उस पहादेत्यक्रे रक्तस प्रकट हुए असुरोद्वारा सम्पूर्ण जगत्‌ व्याम हो गया। इससे देवताओंकों बड़ा भय हूझग
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3139)
- **Original**: देवताओंको ठदास देख चण्डिकाने कालीसे शीक्षतापूर्वक कहा--' चामुण्डे ! हुम अपना मुख और भो फैलाओ
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3140)
- **Original**: तथा मेरे शस्त्रपातसे छपी 5 के गिरनेवाले रक्तबिन्दुओं और उनसे उत्पन्न होनेवाले
- **Translation**: 

---

