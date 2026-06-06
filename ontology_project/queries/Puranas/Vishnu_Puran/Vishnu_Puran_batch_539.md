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

### Verse 1 (Vishnu Puran 0.10761)
- **Original**: 4 श्रीपराशरजी बोले--अपने कार्योंसे पृचिवीको विचलित करनेवाले, बड़े विकट कार्य करनेवाले, घरणीधर ज्ोषजीके अवतार माया-मानवरूप महात्मा अल्वशमजीको गोपोंके साथ बनमें बिचरते देख उनके उपभोगके लिये बरुणने बारुणी (मदिरा) से कहा--
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10762)
- **Original**: “हे मदिरे ! जिन महाबलूशाल्मो अनन्त देवको तुम सर्वदा प्रिय हों; हे शुभे ! तुम उनके उपभोग और प्रसन्नताके छिये जाओ''
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10763)
- **Original**: वरुणकी ऐसी आज्ञा होनेपर वारूणी बुन्दावनमें उत्पन्न हुए कदस्म-सक्षके कोटरमें रहने लूंगी।4
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10764)
- **Original**: आःर5 ) विचरन्‌ बलदेवो5पि मदिरागन्धपुत्तमम्‌ । आधघ्राय मदिरातर्षमब्रापाथ वरानन:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10765)
- **Original**: 5 ततः कदम्बात्सहसा मद्यधारां स लाडुली । पत्ती वीक्ष्य मैत्रेय प्रययौ परमां मुदप्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10766)
- **Original**: 6 पपौ च गोपगोपीभिस्समुपेतो मुदान्यित: । प्रगीयमानो ललित गीतवाह्मयविज्ञारदैः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10767)
- **Original**: 7 स्‌॑ पत्तोउ्यत्तधर्माम्भ: कणिकामौक्तिकोज्ज्वलः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10768)
- **Original**: आगच्छ यपुने स्त्रातुमिच्छामीत्याह विज्डलः ।
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10769)
- **Original**: 8 तस्य वाचं नदी सा तु मत्तोक्तामबमत्य वै । नाजगाम ततः क्ुद्धों हलं जग्राह लाड़ूल्ली
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10770)
- **Original**: 9 गृहीत्वा तां हलान्तेन चकर्ष पदचिद्नल: । पापे नायासि नायासि गम्यतामिच्छयान्यत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10771)
- **Original**: 10 साकृष्टा सहसा तेन मार्ग सनत्यज्य निम्नगा । यत्रास्ते बल्भद्रोडसों प्लावयामास तद्दनम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10772)
- **Original**: 11 शरीरिणी तदाभ्येत्य आसबिद्वललोचना । प्रसीदेत्यश्रवीद्राम॑ मुझ मां सुसलायुध
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10773)
- **Original**: 12 ततस्तस्था: सुबच्ननमाकर्ण्य स हलायुध: । सो5ब्रवीदबजानासि मम शौर्यब्रले नदि। सो5हं त्वां हलपातेन नविष्यामि सहस्तधा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10774)
- **Original**: 13 श्रपराशर उकाच इत्युक्तयातिसन्त्तासात्तया नद्या प्रसादित: । भूभागे प्लाविते तस्मित्युमोच यपुनां खल:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10775)
- **Original**: 94 ' ततस्स्त्रातस्थ वे कान्तिरजायत महात्यन:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10776)
- **Original**: 15 अवतंसोत्पलं चारु गृहीत्वैंक च कुण्डलम्‌ । वरुणप्रहितां चास्मै मालामम्लानपड्भुजाम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10777)
- **Original**: समुद्राभे तथा वस्त्रे नीले लक्ष्मीरयच्छत
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10778)
- **Original**: 16 कृतावत॑सस्स तदा चारुकुण्डलभूषित: । नीलाम्बरधरस्स्रग्वी शुझुभे कान्तिसंयुत:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10779)
- **Original**: 17 इत्थे बिभूषितों रेसे तत्र रामस्तथा व्रजे । मासद्येन यातञ्ष स पुनर्दारकां पुरीम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10780)
- **Original**: 18 रेव्ती नाम तनयां रैवतस्य महीपते: । उपयेमे बलस्तस्यां जज्ञाते निशठोल्मुको
- **Translation**: 

---

