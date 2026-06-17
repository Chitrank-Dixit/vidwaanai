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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.101)
- **Original**: 1 कुक्षी तु सागर: सप्त सप्तद्ीपा वसुन्धरा । पृथिव्यां यानि तीर्थानि कलशस्थानि तानि वै
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.102)
- **Original**: गंगा गोदावरी कृष्णा गोमती सरयू यथा । नर्मदा यमुना ताप्ती गोमती च सरस्वती
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.103)
- **Original**: ऋग्वेदोडथ यजुर्वेद: सामवेदो हाथर्वण: । अज़ैश्च सहिता: सर्वे कलशं तु समाश्रिता:
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.104)
- **Original**: अनत्र गायत्री सावित्री शान्ति: पुष्टिकरी तथा । आयान्तु मम शान्त्यर्थ पापानां क्षयकारका:
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.105)
- **Original**: कलश प्रार्थना देव-दानव-सम्वादे मध्यमाने महोदघौ । उत्पन्नोठसि तदा कुम्भ ! विधृतों विष्णुना स्वयमू
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.106)
- **Original**: त्वत्तोये सर्वतीर्थानि देवा: सर्वे त्वयि स्थित: । त्वयि तिष्ठन्ति भूतानि त्वयि प्राणा: प्रतिष्टिता:
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.107)
- **Original**: शिव: स्वयं त्वमेवासि विष्णुस्त्वन्ञ प्रजापति: । आदित्या वसवो रुद्रा विश्वेदेवा: सपैतूकाः
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.108)
- **Original**: वरुण प्रार्थना त्वयि तिष्ठन्ति सर्वेजपि यतः कामफलप्रदः । त्वत्प्रसादादिमां पूजां कर्तुमी है जलोद्धव !
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.109)
- **Original**: सात्रिध्यं कुरु मे देव ! प्रसत्नो भव सर्वेदा । विश्वकमर्चिनि यज्ञ कृपां कुरु विशेषतः
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.110)
- **Original**: ... श्री विश्वकर्मा पुराण एवं पूजन पद्धति... 75] विश्वकर्सा पुराण एवं पूजन पद्धति 5
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.111)
- **Original**: नमो नमस्ते स्फटिकप्रमाय सुश्वेतहाराय सुमंगलाय । सुपाशहस्ताय झषप्रियाय जलाधिनाधाय नमो नमस्ते
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.112)
- **Original**: अथ विश्वकर्मण: प्राण-प्रतिष्ठा विधिवत्‌ कलश स्थापन के वाद 2 का विश्वकर्मा जी की धातुमयी, प्रस्तरमयी ट्र्ण प्राण '्फ़ अथवा मृण्मयी मूर्ति में निम्नलिखित प्रकार ं से प्राण प्रतिष्ठा करनी चाहिए। साथ ही- बिक /
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.113)
- **Original**: ... काष्ठपीठ अथवा वेदी पर विश्वकर्मा बनाकर किला शक पंचोपचार से पूजन भी करना चाहिए। बसु दोष आर्मि इंसके पूर्व अपनी शरीर शुद्धि के लिए षड़ज न्यास इस प्रकार करे- . ' ऊँ वां हृदयाय नमः । ऊँ वीं शिरसे स्वांहा । उँ0 वूं शिखायै वषट्। ऊँ वैं कवचाय हुमू । ऊँ वीं नेत्रन्याय वौषटू । ऊँ वः अस्त्राय फट
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.114)
- **Original**: ऊँ वां अंगुष्ठाभ्यां नमः
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.115)
- **Original**: ऊँ वीं तर्जनीभ्यां नमः । ऊँ वूं मध्यमाभ्यों नमः । ऊँ वैं अनामिकाभ्यां नमः । ऊँ वौं कनिष्ठिकॉ््यां नमः: । डे: व: करतलकरपूथ्ठाभ्यां फट । तत्रादौ विनियोग :' अस्य श्रीप्राणप्रतिष्ठामंत्रस्य ब्रहम-विष्णु-महेश्वरा ऋषयो ऋग्युजः सामाधर्वण: छन्दांसि चैतन्यरूपा अपरा प्राणशक्तिर्देवता आं बीज हीं शक्ति: क्रों कीलकम्‌ श्रीविश्वकमदिवस्य प्राणप्रतिष्ठापने विनियोग: । करन्यास: 1.ऊँजांहींक्रोंअंकंखंगंपंडंक्रों हीं आंपृथिव्यप्तेजोवाय्वाकाशात्मने आं उंगुष्ठाभ्यां नमः । कक _* & _* . * 4 क्रोउंटठंडंढ ऊँ मध्यमाम्यां नमः । 4. ऊँ आंहींक्रोंएंतंधंदंधंनंक्रों हीं आं वाकूपाणिपादापायूपस्थाने ऐं अनाभिकाग्यां नमः । 5. ऊँ हीं क्रों औ पंफंबं भं मं क्रों हीं आं वचनादानगतिविसर्गानिनदात्मने औँं कनिष्ठिकाम्यां नमः । अर एव ज्दंके पी पं पड पर स्व सा डर था पर लो सि पा 6. आया क्री पग दल नहा एच रऊ क दी जो मनोहंकारचित्तविज्ञानात्मने अ: करतलकरपृष्ठाभ्यां नम: । 76 श्री विश्वकर्मा पुराण एवं पूजन पद्धति ः
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.116)
- **Original**: हदयादिन्यास पूर्ववत्‌ क्रमशः मन्त्ोच्चारण पूर्वक 1. आं हदयाय नमः । 2. ई शिरसे स्वाहा
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.117)
- **Original**: ऊं शिखायै वषट्‌। 4. ऐं कवचाय हुम्‌। 4. औ नेत्रबयाय वौषट्‌ । 6. अ: अस्त्राय फटू। इत्यादि मन्त्रों से हदयादि न्यास करे। हाथ में अक्षत-पुष्प लेकर- ऊँआंहीक्रोंअंयंरंतंवंशंष॑संहंक्षं अंज:क्रोंहींआं श्रीविश्वकमदिवस्य इह प्राणा इह प्राणा: । ऊँआंहींक्रोंअंयंरंतलंवंशंष॑संहंक्ष॑जंअःक्रोंहीं आं श्रीविश्वकमदिवस्य जीव इह स्थित: । ऊँजआंहींक्रोंजंयंरंलंवंशंषंसंहंक्षं अ: क्रो हीं आं श्रीविश्वकमदिवस्य सर्वेन्द्रियाणि वाडू-मनः-त्वक्‌ू-चक्षुः-श्रोज-जिह्लाग्राणपाणिपादापायूपस्था इठैवागत्य सुखं चिरं तिष्ठन्तु स्वाहा । इसके बाद अंजलि में पुष्प लेकर प्राणशक्ति का ध्यान इस प्रकार करे- रक्ताम्भो घिस्थपोतोल्लसदरुण सरो जाधिरूदाकराब्जैः, पाशंकोदण्ड- मिक्षुद्ववगुणमणिमय्यंकूश॑ पच्नबाणान्‌ । विध्ाणस्रक्कपालं न्िनयनलसितापी- नवक्षोरुहादू्ां , देबीदालार्क वर्ण भवतु सुखकरी प्राणां शक्ति: परान्न: । अंजलि का पुष्प चढ़ाकर अक्षत से पुनः विश्वकर्मा जी को प्रतिष्ठापन करे । ऊँ मनोजूतिर्जुषतामाज्यस्य बृहस्पतिय॑ज्ञमिमन्तनोत्वरिष्ट यज्ञश्4 समिमं दधातु । विश्वेदेवा स इह मादयन्तामो प्रतिष्ठ
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.118)
- **Original**: अस्यै प्राणा: प्रतिष्ठन्तु अस्ैं प्राणा: क्षरन्तु च । अस्वै देवत्वमचवि सामहेति च कश्चन स्वाहा । अस्मिनू कलशे (विद्यां वा; श्रीविश्वकर्मन्‌ ! सुप्रतिष्ठितों वरदो भव । . इस प्रकार प्राण प्रतिष्ठा करके पुनः ध्यांन करना चाहिए यथा-- ऊँ दंशपाल महावीर ! सुचिन्रकर्मकारक । विश्वकृत्‌ विश्वघृकू च त्व॑ं वसना मानदण्डधृकू । भी. विश्वकर्मनू ! इहागच्छ इह. तिष्ठ, अन्नाधिष्ठान॑ कुरूं कुरु मम पूजा गृहाण। हे विश्वकर्मा जी ! यहां आइए, इस सुन्दर मूर्ति में विराजिए और कृपया मेरी अर्चना (पूजा) स्वीकार कीजिए । अब मैं आपका यहां प्रार्थना पूर्वक घोडशोपचार से पूजन करता हूं। देवशिल्पिनू महाभाग देवानां कार्यसाधक ! विश्वकर्मन्‌ू ! नस्तुम्य॑ं. सर्वाभीष्टप्रदायक !
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.119)
- **Original**: उपर्युक्त विधि से विश्वकर्मा जी का प्राण प्रतिष्ठा पूर्वक ध्यान करके निम्नलिखित पोडशोपचार से उनकी पूजा करनी चाहिए । आवाहन--आवाहयामि देवेशं विश्वकर्माणमीश्वरमु। मूर्ताड मूर्तकरं * देव॑ सर्वकत्तारमदूमुतमू
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.120)
- **Original**: . श्री विश्वकर्मा पुराण एवं पूजन पद्धति... 7] विश्वकर्मा पुराण एवं पूजन पद्धति फय्र
- **Translation**: 

---

