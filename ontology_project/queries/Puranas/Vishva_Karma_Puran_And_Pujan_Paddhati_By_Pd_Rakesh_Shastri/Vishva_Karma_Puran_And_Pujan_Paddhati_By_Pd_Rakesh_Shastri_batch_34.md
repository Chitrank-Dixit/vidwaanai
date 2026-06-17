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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.661)
- **Original**: चालिस दिन जो ध्यान लगावै। राजद्रोह से . सुक्ति पावै
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.662)
- **Original**: भूत प्रेत नहिं उनहिं सतावे।
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.663)
- **Original**: श्री विश्वकर्मा पुराण एवं पूजन पद्धति 203
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.664)
- **Original**: चालीसा में जो मन लावै
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.665)
- **Original**: धूप देय ऊर्रु जपे हमेशा । फिर नहिं पावै दुःख लवलेशा
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.666)
- **Original**: जो कोई अक्षत पुष्प चढ़ावै। होय मुक्त जग फिर नहिं आवै
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.667)
- **Original**: उसके जीवन का रखवारा। रहे नित्य विश्वकर्मा प्यारा 0. सकल पदारथ करतल ताके। बसे हृदय विश्वकर्मा जाके
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.668)
- **Original**: दोहा-जआदि सृष्टि आघार तुम,रचना विविध प्रकार । नाथ तुम्हारी कृपा बिन, केहिं विधि उत्तरूं पार
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.669)
- **Original**: हाथ जोड़ विनती कर, धखं चरण माथ
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.670)
- **Original**: पूर्ण होय मम कामना, यह वर दीजै कर्तारि
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.671)
- **Original**: श्री विश्वकर्मा जी की आरती न ज्योततिर्मय शान्तमयं प्रदीप्त॑ विश्वात्मकं विश्वजीतन्िरीशं । आइधंत शून्य॑ सकलैक नाथ॑ श्री विश्वकर्माणमहं नमामि
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.672)
- **Original**: . ऊँ विश्वकर्मा दिशां पतिः सनः पशून्यातु सो5स्मान्यातु तस्मै नमः । प्रजापतिकद्रो वरुणीग्निर्दिशांपति: सनः पशुन्यातु सोडस्मान्पातु तस्मै नमः
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.673)
- **Original**: अथ पुरुषोह वै विश्वकर्मणे कामयत प्रजासूजयैति । विश्वकर्मण: प्राण जायते मनः सर्वोन्द्रियाणि च। खवायुजर्यों विराम: पृथिवी विश्व॑स्यघारिणी
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.674)
- **Original**: विश्वकर्मणो ब्रह्मा जायते । विश्वकर्मणो रुद्रो जायते । विश्व कर्मणो नारायणों .. जायते । विश्वकर्मण: प्रजापतयः प्रजायनते । विश्वकर्मणो दादशादित्या रुद्रा वसवः सर्वे देवता: सर्वे ऋषयः सर्वाणि छन्दांसि सर्वाणि भूतानि वा समुत्पचन्ते । विश्वकर्मणी प्रवर्धते । विश्वकमणि प्रतीयन्ते । ऊँ अथ नित्यो देवो एको विश्वकर्मा । यो देवानां नामघारी एक एवं विश्वकर्मा । विराट विश्वकर्मा । स्वराट विश्वकर्मा । सम्राट विश्वकर्मा ) अथ रुद्रो विश्वकर्मा । ब्रह्मा विश्वकर्मा । शिवश्च विश्वकर्मा । विष्णुश्च विश्वकर्मा । शक्रश्च विश्वकर्मा । थावापृथिव्यौ च विश्वकर्मा । कालश्च विश्वकर्मा । विशश्च विश्वकर्मा । दिक्र च विश्वकर्मा । अग्निश्व विश्वेकर्मा । ऊर्घ्वश्व विश्वकर्मा । 'अधश्च विश्वकर्मा । अवांतटश्च विश्वकर्मा । अंतर्वहिश्च विश्वकर्मा । विश्वकर्मणो 204 श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.675)
- **Original**: निराकृति! पुण्डरीक विज्ञान घनम्‌ । तस्मातू तदिदावनमात्रं ब्रह्मणयो विश्वक्मोमू ।
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.676)
- **Original**: विश्वकर्मण: एवेदं सर्व । यत्‌ भूतं यच्च भव्यं । निष्कलंको निरंजनो निर्विकल्पों निराख्यातः
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.677)
- **Original**: शुद्धादैतैका विश्वकर्मा न दितीयोस्ति कश्चितू । य एवं वेद स विश्वकर्मारडभवत्ति
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.678)
- **Original**: ऊँ इत्यग्े व्याहरेतू । नमेति पश्चात । विश्वकर्मण इव्यष्यक्षरं पद॑ ध्येति । अन प्रब्रवस्सर्व आयुरोत। विदंते प्राजापत्य॑ रायस्पोख गौपत्यं
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.679)
- **Original**: तततो अमृततत्वमुश्नुते । ततो अमृतत्तत्वमश्नुत इति च एवं वेद । प्रत्यगानंद ब्रह्म पुरुष॑ प्रणव स्वरूपमू अकार, उकारो, मकार इति। तानेकधारममरत्तदेतदोमिति । यमुक्त्वा मुच्वते योगी जन्मसंसार वंघनातु
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.680)
- **Original**: के नमो विश्वकर्मण :इति मंगोपसकः सायुज्ये गमिष्यति । तदिदूं पर सर्वमूतास्थमेकं विश्वकर्माण कारणरूए मकार परविश्दब्रह्मोम । पद्र विष्यवा . ख्यसिति तेपि विश्वकर्मकोपनिषद्भ । यो हवै विश्वकर्मणयो पनिषदभघीते । सर्वेभ्यो पोपेश्यो विमुक्तो शवति। ससर्वेभ्य: वियुक्तः सर्वान्कामानवाप्नोति ब्रह्मत्व॑ च गच्छति । इत्सुपनिषत्तू
- **Translation**: 

---

