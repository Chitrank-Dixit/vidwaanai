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

### Verse 1 (Markende Puran 0.2441)
- **Original**: एबं संक्षीयमाणे तु स्वसैन्यें महिषासुरः। माहिषेण स्वरूपेण त्रासद्याप्रास त्ानू गणान्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2442)
- **Original**: 3. गरा>-खग्डखण्डं। (97 कांश्िित्तुण्डप्रहारेण. खुरक्षेपैस्तथापयन्‌। लाडूलताडितांश्वान्याउ्छुज्डा भ्यां चल चिदारितानू
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2443)
- **Original**: चेगेन कांश्ििदपरान्नादेन भ्रमणेन चजत्ञ। निःश्वासपतनेनान्यान्‌ पातवब्ामास भूतले
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2444)
- **Original**: निपात्य प्रम्थ्नानीकमभ्यधावत सोउसुर:। सिंहं हन्तुं महादेब्या: कोप॑ चक्रे ततोउम्लिका
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2445)
- **Original**: मो$पि कोपान्महावीर्य: खुरक्षुणएणमहीलल: । श्रृड़ाभ्यां पर्वतानुच्चांश्रिक्षेप च्र ननाद च्
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2446)
- **Original**: वेगभ्रमणविश्षुणणा मही तस्य व्वशीर्यत्त। लाडूलेनाहतश्ञाब्थिः प्लाब्यामास सर्वतः
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2447)
- **Original**: धुतश्रृड्भविभिन्नाश्च खण्ड! खएड़ ययुर्घना: । श्रासानिलास्ता: शतशो निपेतुर्नभसो चला:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2448)
- **Original**: इत्ति क्रोधस्रमाध्मातमापतन्तं प्रहासुरम्‌।
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2449)
- **Original**: दूष्ठा सा चणिडिका कोप॑ तद्गधाथ तदाकरोतू
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2450)
- **Original**: सा क्षिप्चा तस्य से पाशं ते बबन्ध महासुरम्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2451)
- **Original**: तंत्वाज माहिष॑ रूप॑ स्रोंडपि बद्धो महापृथे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2452)
- **Original**: तत: सिंहो5भवत्सद्यो यावन्तस्थाम्बिका शिए:। छिनत्ति तावत्पुरूप: खड्गपाणिरदृश्यत
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2453)
- **Original**: तंत एवाशु पुरूष देवी चिच्छेद सायकैः। ले खड़गचर्मणा सार्द्ध त्तः सोउभून्मसहागज:
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2454)
- **Original**: करेण जन महासिंह तं॑ चक्तर्ष जगर्ज च। कर्षतस्तु करे देवी खड्गेन निस्‍्कृन्तत
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2455)
- **Original**: ज़तो महासुरों भूयो माहिषं वपुरास्थित:। तश्नेव क्षोभयामास जैलोक्य सच्तराचरम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2456)
- **Original**: तत्ः क्रुद्धा जगन्माता चण्डिका पानपुत्तपम्‌। पपौ पुत्र: पुनश्नैव जहासारुणलोचना
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2457)
- **Original**: ननर्द चासुरः सोडपि बलबीर्यमंदोद्भत:। बिषाणाध्यां च चिक्षेप चणिडकां प्रति भुधग्रन्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2458)
- **Original**: स्नाच तान्‌ ग्रहितांस्तेन चुर्णयन्ती शरोत्कर:।
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2459)
- **Original**: उब्ाच्च॒ त॑ मदोदधूलमुखरगाक़लाक्षरम्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2460)
- **Original**: इस्र प्रकार अपनी सेनाका संहार होता टेग्व्
- **Translation**: 

---

