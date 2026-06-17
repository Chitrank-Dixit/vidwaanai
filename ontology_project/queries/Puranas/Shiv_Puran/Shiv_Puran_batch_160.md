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

### Verse 1 (Shiv Puran 0.3181)
- **Original**: इह भुक्‍्त्वाखिलान्‌ भोगानन्ते मुक्ति छ्ेस्न सः
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.3182)
- **Original**: आ पएतब्छियपुणणस्थ॒ वक्तु।.. प्लेतुश ख्रगणः ससुतः स्राम्बः ज करोतु स इंकरः
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.3183)
- **Original**: (हिल फ या+ संष् 0 स्क0 49
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.3184)
- **Original**: 43--51) व्यासजी कहते है--अथह हिवपुराण पूरा हुआ, इस हितकर पुराणको बढ़े आदर एबं सुनना चाहिये। नास्तिक, भ्रद्धाहीन, जझठ, महेश्वरके प्रति अक्तिसे रहित तथा धर्मध्यजी (पास्वण्डी) के इसका उपदेदा नहीं देना चाहिये । इसका एक जार अवण करनेसे ही सारा पाप भस्म हो जाता है। भक्तिहीन भक्ति पाता है और भक्त भक्तिकी समृझ्ठिक्ा भागी होता है। दोबारा अवण करनेपर उत्तम भक्ति और तीसरी बार सुननेपर मुक्ति सुलूभ हो जाती है, इसलिये मुमुक्षु पुरुषोंकों चारंबार इसका श्रवण करना चाहिये। किसी भी उत्तप फलतको पानेके लिये शुद्ध-बुम्द्िसि इस पुराणकी पाँच आवृत्ति करनी चाहिये
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.3185)
- **Original**: ऐसा करनेसे मनुष्य उस फलक्ो प्राप्त कर लेता है, इसमें संदाद्य नहीं है। प्रात्नीन कालके राजाओं, ब्राह्मणों तथा श्रेष्ठ लैइयोंने इसकी स्लात आवृत्ति करके शिवका साक्षात्‌ दर्शान श्राप्त किया है। जो मनुष्य भक्तिपरायण हो इसका अ्रवण करेगा, वह भी इहल्म्ेकमें सप्पूर्ण भोगोंका उपभोग करके अन्‍्तमें मोक्ष त्राप्त कर छेणा
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.3186)
- **Original**: यह श्रेष्ठ शिवपुराण भगवान्‌ शिवको अत्यन्त प्रिय है। यह बेदके तुल्य माननीय, भोग और मोक्ष देनेब्राल्ला तथा भक्तिभावको ब्रढ़ानेताला है। अपने अ्रमथगणों, दोनों पुत्रों तथा देवी पार्वतीजीके साशथ्र भगवान्‌ झंकर इस पुराणके वक्ता और ओताका सदा कल्याण करें। (अध्याय 421) है
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.3187)
- **Original**: बायवीयसहिता सम्पूर्ण
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.3188)
- **Original**: शिवपुराण सम्पूर्ण
- **Translation**: 

---

