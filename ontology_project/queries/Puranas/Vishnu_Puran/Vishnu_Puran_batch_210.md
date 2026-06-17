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

### Verse 1 (Vishnu Puran 0.4181)
- **Original**: 36 सर्वविज्ञानसम्पन्न: सर्वशास्त्रार्थतत्त्ततित्‌ । अपश्यत्स च मैत्रेय आत्मान॑ प्रकृते: परम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4182)
- **Original**: 37 आत्पनो5ध्िगतज्ञानो टेवादीनि महामुने । सर्वभूतान्यभेदेन स॒ ददर्श तदात्मन:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4183)
- **Original**: 38 न पपाठ शुरुष्रोक्ते कृतोपनयन: श्रुतिम्‌। न ददर्श च कर्माणि शास्त्राणि जगृहे न तु
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4184)
- **Original**: 39 उक्तो5पि बहु: किज्धिजडवाक्यमभाषत । तदप्यसंस्कारगुणं ग्राम्यवाक्योक्तिसंश्रितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4185)
- **Original**: 40 अपध्वस्तवपु: सो5पि मलिताम्बरधृग्द्रिज: । क्लित्रदन्तान्तर: सर्वे: परिभूत: स नागरैः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4186)
- **Original**: 41 सम्मानना परां हानि योगड्ें: कुरुते यतः । जनेनावमतो योगी योगसिर््धि च विन्दति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4187)
- **Original**: सम्मान ही है, जो योगी अन्य मनुष्योंसे अपमानित होता जब बह उनके निकट आ जाता तो उसके प्रेमसे उनका मुख खिल जाता था
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4188)
- **Original**: इस प्रकार उसोमें आसक्तचित्त रहनेसे, राज्य, भोग, समृद्धि और स्वजनॉंकों स्याग देनेबाले भी गजा भरतकी सपाधि भंग हो गयी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4189)
- **Original**: उस राजाका स्थिर चित्त उस मृगके चख्जल होनेपर चद्धल हो जाता और दूर चले जानेपर दूर चला जाता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4190)
- **Original**: क्रालान्तरमें ग़जा भरतने, उस मृगबालकटद्ठाय पुत्रके
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4191)
- **Original**: सजल नयनोंसे देखे जाते हुए पिताके समान अपने प्राणोंका त्याग किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4192)
- **Original**: हे मैत्रेस ! राजा भी प्राण ऊेड़ते समय स्लेहबश उस मृगक्तों ही देखता रहा तथा उसीमें तन्‍्मय रहनेसे उसने और कुछ भो चिन्तन नहीं किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4193)
- **Original**: तदनन्तर, उस समयकी सुदृढ़ भावनाके कारण बह जम्बूमार्ग (कालझ्रपर्वत) के घोर बनमें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4194)
- **Original**: अपने पूर्वजत्मकी स्मृतिसे युक्त एक मृग हुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4195)
- **Original**: हे ट्विजोत्तम ! अपने पूर्वजन्पका स्मरण रहनेके कारण वह संसारसे उपरत हो गया और अपनी माताकों छोड़कर फिर शालकम क्षेत्रमें आकर ही रहने छगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4196)
- **Original**: वहाँ सूखे घास फूँस और पत्तोंसे ही अपगा दारौर पोषण करता हुआ खड अपने मगत्व-प्रप्तिके हेतुभूत कर्मोंका निराकरण करने लगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4197)
- **Original**: तदनन्तर, उस चारीरकों छोड़कर उसने सदाचार-सम्पतन्न योगियोंके पत्रित्र कुलमें ब्राह्मण-जन्म ग्रहण किया। उस टेहमें भो उसे अपने पूर्वजन्मका स्मरण बना रहा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4198)
- **Original**: है मैत्रेय ! बह सर्वविज्ञानसग्पन्न और समस्त झाखनोंके मर्मको जाननेवाल्त्र था तथा अपने आत्माको निरन्तर प्रकृतिसे परे देखता था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4199)
- **Original**: हे महामुने ! आताज्ञानसम्पन्न होनेके कारण वह देवता आदि सम्पूर्ण प्राणियोंकों अपनेसे अभिन्नरूपसे देखता था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4200)
- **Original**: उपनयन-संस्कार हो जानेपर वह गुरुके पढ़ानेपर भो वेद-पाठ नहों करता था तथा न किसी कर्मकी ओर ध्यान देता और न कोई अन्य शास्त्र ही पढ़ता था
- **Translation**: 

---

